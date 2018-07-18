#--------------------------------------------------
#  IMPORT MODULES
#--------------------------------------------------
from pymongo import MongoClient
import re

#--------------------------------------------------
#  CONNECT TO DATABSE
#--------------------------------------------------
mongo_client = MongoClient()
mongo_dbs = mongo_client['testdb3']
mongo_coll = mongo_dbs['brexit']
cursor = list(mongo_coll.find())

#--------------------------------------------------
#  EXTRACT TWEET TEXT
#--------------------------------------------------
# Take out a few elements
regex_str = [r'http\S+', r'\n']
regex = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

sentences = []
for d in cursor:
    tweet = d.get('text') or d.get('text_rt')
    tweet = regex.sub('', tweet)
    tweet = tweet.lower()
    sentences.append(tweet)

#--------------------------------------------------
#  STORE TWEETS INTO TEXTFILE
#--------------------------------------------------
with open('../../dataset/corpus/all_tweets.txt', 'w', encoding='utf-8') as f:  # TXT FILE
    for sent in sentences:
        f.write('{}\n'.format(sent))


