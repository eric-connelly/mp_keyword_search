# cs410_project

## Motivation
Mountain Project is a website used by rock climbers to document climbing routes around the world. Mountain project already has search functionality, allowing a user to search routes by location, type, difficulty, user rating, and number of pitches (see www.mountainproject.com/route-guide). What the route finder lacks, however, is the ability to search by keyword. This project implements a basic keyword search over Moutain Project climbs.

## Dependencies
#### Python 3
#### Nonstandard Python libraries
- beautifulsoup4
- metapy

Use the following to ensure everything is up to date.
```
pip install --upgrade pip
pip install metapy beautifulsoup4
```
#### System
Currently, the software is only tested on Linux, but it should work on any UNIX-based OS.

#### Mountain Project Account
The software uses the Mountain Project API to search for the routes fitting your parameters. In order to use it, you'll need a Mountain Project account so you can use your private key to run the search. Go to www.mountainproject.com to create an account. You can then log in and navigate to www.mountainproject.com/data to find your private key.

## Usage
1. Edit `search_config` to contain the parameters of your choosing. More detailed instructions and sample parameter values are contained in the file. Parameters include:
   - private key
   - latitude
   - longitude
   - maximum distance searched
   - maximum results
   - minimum difficulty of route
   - maximum difficulty of route
   - query
2. Run `./run.sh` in order to pull the relevant data from Mountain Project, create the inverted index, and search for your query. Simple results are immediately output to the terminal, with more detailed results in `results.txt`.
3. If you would like to keep all of the parameters the same and search the same set of climbs using a different query, you can simply run
```
python rank.py "your query"
```

## Known Issues/Future Work
The process of finding climbs and scraping the webpage for each climb is very slow. Every time a user wants to change a parameter, the finding and scraping process must be redone and the inverted index rebuilt. This results in a lot of wasted time. In future versions, the entirety of Mountain Project will be scraped ahead of time and the API's search feature rebuilt in this software. This will allow the inverted index to be prebuilt, saving the user both time and the need to have their own private key to use the Mountain Project API.
