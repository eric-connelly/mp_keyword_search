# Script to run everything. Simply use ./run.sh

. search_config

python3 make_corpus.py $key $latitude $longitude $maxDistance $maxResults $minDifficulty $maxDifficulty

echo "Corpus created!"

python3 rank.py $query
