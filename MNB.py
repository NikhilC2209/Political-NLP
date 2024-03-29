# -*- coding: utf-8 -*-
"""5.sentiment_analysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1OPQDDJTKy0b40pziZWSsoBCmQV6HyXsm
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

df = pd.read_csv("MNB_sentiments.csv")

leaders = ['narendramodi','SwamiPMaurya','yadavakhilesh','shivpalsinghyad','AjayLalluINC','kpmaurya1','ptshrikant' ]

#df['sentiment'] = df['sentiment_score'].apply(sentiment_grouping)
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