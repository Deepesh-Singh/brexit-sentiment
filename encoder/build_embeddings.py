#--------------------------------------------------
#  IMPORT MODULES
#--------------------------------------------------
import torch
import numpy as np
from datetime import datetime

#--------------------------------------------------
# LOAD FACEBOOK MODEL
#--------------------------------------------------
# -- LOAD ENCODED MODEL --
infersent = torch.load(
    'infersent.allnli.pickle', map_location=lambda storage, loc: storage
)
# -- LOAD TOKS --
infersent.set_glove_path('../dataset/GloVe/glove.840B.300d.txt')

#--------------------------------------------------
#  LOAD TWEETS
#--------------------------------------------------
sentences = []
labels = []
with open('../dataset/corpus/annotated_tweets.txt', 'r', encoding='utf-8') as f:
    index = 0
    for tweet in f.readlines():
        tweet_text = tweet.split(';class;')[0]
        label = tweet.split(';class;')[1]
        label = int(label.strip('\n'))
        labels.append(label)
        sentences.append(tweet_text)
        index += 1
with open('../dataset/corpus/annotated_tweets_05_28.txt', 'r', encoding='utf-8') as f:
    index = 0
    for tweet in f.readlines():
        tweet_text = tweet.split(';class;')[0]
        label = tweet.split(';class;')[1]
        label = int(label.strip('\n'))
        labels.append(label)
        sentences.append(tweet_text)
        index += 1

#--------------------------------------------------
#  BUILD EMBEDDINGS
#--------------------------------------------------
# -- BUILD VOCABULARY --
infersent.build_vocab(sentences, tokenize=True)
# -- BUILD WORD EMBEDDINGS --
embeddings = infersent.encode(sentences, tokenize=True)

#--------------------------------------------------
#  SAVE TWEET EMBEDDINGS AND LABELS
#--------------------------------------------------
np.save('../dataset/startramp/embeddings', embeddings)
with open('../dataset/startramp/labels.txt', 'w') as f:
    for l in labels:
        f.write(str(l) + '\n')
