import urllib.request
import json

class Puller():
    def __init__(self,key,lat,lon,maxDistance=30,maxResults=500,
                    minDiff="5.6",maxDiff="5.14"):
        self.description = "Pulls climbs based on input parameters"
        self.key = key
        self.lat = lat
        self.lon = lon
        self.maxResults = maxResults
        self.maxDistance = maxDistance
        self.minDiff = minDiff
        self.maxDiff = maxDiff
    def get_climbs(self):
        # gets climbs from Mountaian Project API based on object parameters
        # returns dict with list of climbs
        url = "https://www.mountainproject.com/data/" + \
                "get-routes-for-lat-lon" + \
                "?lat=" + str(self.lat) + \
                "&&lon=" + str(self.lon) + \
                "&&maxResults=" + str(self.maxResults) + \
                "&&maxDistance=" + str(self.maxDistance) + \
                "&&minDiff=" + self.minDiff + \
                "&&maxDiff=" + self.maxDiff + \
                "&&key=" + self.key
        with urllib.request.urlopen(url) as webpage:
            page_data = json.loads(webpage.read().decode('utf-8'))
            return page_data
