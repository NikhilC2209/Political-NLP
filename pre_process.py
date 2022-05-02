import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re

tweets_df = pd.read_csv("old_tweets.csv")

print(tweets_df.head())

#print(tweets_df['Text'][1])
tweets_df['tokens'] = ""

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

for i in range(len(tweets_df)):
    for token in tweets_df["tokens"][i]:
        r = remove_links(token)
        if r:
            tweets_df["tokens"][i].remove(token)

for i in range(0,len(tweets_df)):
    tweets_df['Text'][i] = " ".join(tweets_df['tokens'][i])

def final_data():
    return tweets_df
            
