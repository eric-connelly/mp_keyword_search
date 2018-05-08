import sys
import puller
import os.path
import shutil
import json
import urllib.request
from bs4 import BeautifulSoup
import re

# get parameters
key = sys.argv[1]
lat = sys.argv[2]
lon = sys.argv[3]
maxDist = sys.argv[4]
maxResults = sys.argv[5]
minDiff = sys.argv[6]
maxDiff = sys.argv[7]

# remove current idx folder if it exists
if os.path.exists('idx'):
    print("Removing old inverted index")
    shutil.rmtree('idx')

# get climbs, enumerate into dict
print("Pulling climbs from Mountain Project")
route_puller = puller.Puller(key,lat,lon)
climb_list = route_puller.get_climbs()['routes']
climb_dict = {idx: climb for idx, climb in enumerate(climb_list)}
with open('climb_dict.txt', 'w') as climb_file:
    climb_file.write(json.dumps(climb_dict))

# gather relevant climb text, write to file
print("Scraping text from webpages")
with open('climb_text/climb_text.dat', 'w') as corpus:
    for route in climb_list:
        with urllib.request.urlopen(route['url']) as page:
            # parse with BeautifulSoup
            page_html = BeautifulSoup(page, 'html.parser')

            # grab field with description, get description text
            description_box = page_html.find('div', attrs={'class':'mt-2 max-height max-height-md-800 max-height-xs-600'})
            description = description_box.text.strip().split('\n')[-1].lstrip()

            # do the same with the comments
            comment_list_box = page_html.find('div', attrs={'class':'comment-list'})
            comment_box = page_html.find_all('div', attrs={'class':'comment-body max-height max-height-md-300 max-height-xs-150'})
            comment_text = []
            for comment in comment_box:
                comment_text.append(comment.text.strip().split('\n')[0].lstrip())
            comments = ' '.join(comment_text)

            # remove non-ASCII characters and combine all text into one line
            line = re.sub(r'[^\x00-\x7f]',r'', description+' '+comments+'\n')
            corpus.write(line)
