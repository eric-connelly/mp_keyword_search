import sys
import os.path
import metapy
import json

# set query
query_text = sys.argv[1]

# let the user know we're making inverted index if we need to
if not os.path.exists('idx'):
    print("Making inverted index")
idx = metapy.index.make_inverted_index('config.toml')

# run ranker
query = metapy.index.Document()
ranker = metapy.index.OkapiBM25()
query.content(query_text)
num_results = 500 #maximum number of climbs queried
results = ranker.score(idx, query, num_results)

# read in previously output dict of climbs
with open('climb_dict.txt', 'r') as climb_file:
    climb_dict = json.loads(climb_file.read())

# write basic results to terminal, detailed results to file results.txt
with open('results.txt', 'w') as result_file:
    print('Ranking: ')
    for rank, result in enumerate(results, 1):
        climb_info = climb_dict[str(result[0])]
        pitches = climb_info['pitches'] if climb_info['pitches'] != '' else 1
        if rank <= 10:
            print(str(rank) + ': ' + climb_info['name'])
        if rank == 10:
            print('...')
        result_file.write(str(rank) + ': ' +
            climb_info['name'] + '\n' +
            '   ' + climb_info['rating'] + ', ' +
            climb_info['type'] + ' ' + str(pitches) + ' pitch' + '\n' +
            '   ' + climb_info['url'] + '\n\n')
print("\nSee results.txt for more information.")
