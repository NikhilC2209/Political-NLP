import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
from nltk.stem.porter import PorterStemmer
#defining the object for stemming
porter_stemmer = PorterStemmer()

from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

from nltk import pos_tag

tweets_df = pd.read_csv("old_tweets.csv")

print(tweets_df.head())

#print(tweets_df['Text'][1])
tweets_df['tokens'] = ""
tweets_df['pos_tokens'] = ""

for i in range(len(tweets_df)):
 	tweets_df['tokens'][i] = tweets_df['Text'][i].split(" ")

def Party_labels():
    tweets_df['Party'] = "" 
    for i in range(0,101):  
        tweets_df['Party'][i] = "BJP"
    for i in range(101,365):  
        tweets_df['Party'][i] = "SP"
    for i in range(365,466):  
        tweets_df['Party'][i] = "INC"
    for i in range(466,668):  
        tweets_df['Party'][i] = "BJP"

Party_labels()
# print(tweets_df.head())

# # string = "https://t.co/bKRPlqqzA2"
# # string2 = "heh sfjk fdlksjf"

def remove_links(token):
    r = re.match("\Ahttp", token)
    return r


from nltk.corpus import wordnet as wn

def is_noun(tag):
    return tag in ['NN', 'NNS', 'NNP', 'NNPS']


def is_verb(tag):
    return tag in ['VB', 'VBD', 'VBG', 'VBN', 'VBP', 'VBZ']


def is_adverb(tag):
    return tag in ['RB', 'RBR', 'RBS']


def is_adjective(tag):
    return tag in ['JJ', 'JJR', 'JJS']


def penn_to_wn(tag):
    if is_adjective(tag):
        return wn.ADJ
    elif is_noun(tag):
        return wn.NOUN
    elif is_adverb(tag):
        return wn.ADV
    elif is_verb(tag):
        return wn.VERB
    return wn.NOUN

def lemmatizeSentence(token_words):
    #token_words=word_tokenize(sentence) 
    lemma_sentence=[]
    for word in token_words:
        lemma_sentence.append(lemmatizer.lemmatize(word[0], pos=word[1]))
    return lemma_sentence

for i in range(len(tweets_df)):
    for token in tweets_df["tokens"][i]:
        r = remove_links(token)
        if r:
            tweets_df["tokens"][i].remove(token)

for i in range(len(tweets_df)):
    tweets_df['pos_tokens'][i] = pos_tag(tweets_df['tokens'][i])

for i in range(len(tweets_df)):
    for j in range(len(tweets_df['pos_tokens'][i])):
        tweets_df['pos_tokens'][i][j] = list(tweets_df['pos_tokens'][i][j])
        tweets_df['pos_tokens'][i][j][1] = penn_to_wn(tweets_df['pos_tokens'][i][j][1])

for i in range(len(tweets_df)):
    tweets_df["tokens"][i]=lemmatizeSentence(tweets_df["pos_tokens"][i])

for i in range(0,len(tweets_df)):
    tweets_df['Text'][i] = " ".join(tweets_df['tokens'][i])

tweets_df.to_csv("filtered_tweets.csv")

def final_data():
    return tweets_df
            
