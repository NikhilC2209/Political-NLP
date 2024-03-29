# -*- coding: utf-8 -*-
"""Vader.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1BBj5ux1dnAxGcNPatu-ua90qAQkcKCyX
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
from pre_process import final_data

os.getcwd()
one_level_up = os.path.dirname(os.getcwd())
df = final_data()
df

import nltk
nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer
analyser = SentimentIntensityAnalyzer()
df['sentiment_score'] = df['Text'].apply(analyser.polarity_scores)
compound_score = []
sentiment_score = list(df['sentiment_score'])

for i in range(len(df['sentiment_score'])):
    compound_score.append(sentiment_score[i]['compound'])
    
df['sentiment_score'] = compound_score
df

leaders = ['narendramodi','SwamiPMaurya','yadavakhilesh','shivpalsinghyad','AjayLalluINC','kpmaurya1','ptshrikant' ]

def sentiment_grouping(sentiment_compound):
    if sentiment_compound >= 0.05:
        return 'Positive'
    elif (sentiment_compound > -0.05 and sentiment_compound < 0.05):
        return 'Neutral'
    elif sentiment_compound <= -0.05:
        return 'Negative'

df['sentiment'] = df['sentiment_score'].apply(sentiment_grouping)
leader_df = df[df['Username'].isin(leaders)]
leader_df.groupby(['Username', 'sentiment']).count()['Party']
df

leader_sentiment  = leader_df.groupby(['Username', 'sentiment']).count()['Party'].reset_index()
leader_sentiment

leaders = ['narendramodi','SwamiPMaurya','yadavakhilesh','shivpalsinghyad','AjayLalluINC','kpmaurya1','ptshrikant' ]
leader_sentiment.columns  = ['Username','sentiment','num_count']

fig, ax = plt.subplots(2,4, figsize=(15,7))
plt.suptitle('Percentage of Leader Tweets according to Sentiment')
for i in range(ax.shape[0]):
    for j in range(ax.shape[1]):
        count = i*3 +j
        politican = leader_sentiment.Username.unique()
        number_count = leader_sentiment[leader_sentiment['Username'] == leaders[count]].num_count
        label =  leader_sentiment[leader_sentiment['Username'] ==leaders[count]].sentiment
        ax[i,j].pie(number_count, labels = label, autopct='%.1f%%' )
        ax[i,j].set_title(leaders[count])
#plt.savefig(one_level_up + '\\report_graph\\sentiment_analysis')