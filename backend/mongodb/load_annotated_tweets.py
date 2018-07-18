#--------------------------------------------------
#  IMPORT MODULES
#--------------------------------------------------
from pymongo import MongoClient
import re

#--------------------------------------------------
#  CONNECT TO DATABASE
#--------------------------------------------------
mongo_client = MongoClient()
mongo_dbs = mongo_client['testdb3']
mongo_coll = mongo_dbs['brexit']
manual_coll = mongo_dbs['manual_classification_03_11']
cursor = list(mongo_coll.find())
manual_cursor = list(manual_coll.find())

#--------------------------------------------------
#  REGEX COMPILATION
#--------------------------------------------------
# Take out a few elements
regex_str = [r'http\S+', r'\n', r'\r']
regex = re.compile(r'('+'|'.join(regex_str)+')', re.VERBOSE | re.IGNORECASE)

#--------------------------------------------------
#  LOAD INDEX LIST FROM FIRST BATCH
#--------------------------------------------------
with open('../../dataset/labels/current_ids_January_30.txt', 'r', encoding='utf-8') as f:
    label_indices = [int(word.split('\n')[0]) for word in f.readlines()]

#--------------------------------------------------
#  EXTRACT TWEETS
#--------------------------------------------------
tweet_list = []
label_list = []
index = 0
for d in cursor:
    if index in label_indices:
        tweet = d.get('text') or d.get('text_rt')
        tweet = regex.sub('', tweet)
        tweet_list.append(tweet)
        label_list.append(d.get('classification'))
    index += 1

#--------------------------------------------------
# ADD ANNOTATIONS FROM LATER BATCH
#--------------------------------------------------
with open('../../dataset/labels/labels_500_03_11.txt', 'r', encoding='utf-8') as f:
    manual_entry_labels = [int(word.split('\n')[0]) for word in f.readlines()]

d_counter = 0
for d in manual_cursor:
    if d_counter < 500:
        tweet = d.get('text') or d.get('text_rt')
        tweet = regex.sub('', tweet)
        tweet_list.append(tweet)
    d_counter += 1

#--------------------------------------------------
# SAVE TO TEXTFILE
#--------------------------------------------------
complete_label_list = label_list + manual_entry_labels
with open('../../dataset/corpus/annotated_tweets.txt', 'w', encoding='utf-8') as f:
    for index, value in enumerate(tweet_list):
        f.write('{} ;class; {} \n'.format(value, complete_label_list[index]))
