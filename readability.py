import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import textstat
from pre_process import final_data

#final_df = pd.read_csv("old_tweets.csv")

final_df = final_data()

# for i in range(len(final_df)):
#     for token in final_df["Text"][i]:
#         r = remove_links(token)
#         if r:
#             final_df["Text"][i].remove(token)

print(final_df.head())

#final_df["tweets"] = ' '.join([str(i) for i in final_df["Text"]])

def readability_score(text):
    return textstat.automated_readability_index(text)

# print(readability_score("Best wishes of Rajasthan Day to all the residents of Rajasthan, the historical land of bravery, self-respect and sacrifice. The state should move forward on the path of progress, this is the wish."))
# print(readability_score("The MSME Sector is crucial for India’s economic progress. Our Government is taking many steps to add new energy into the sector and support local enterprise. Today’s Cabinet decision is a step in this direction."))
# print(readability_score("Come, let’s celebrate the festival of examinations. Let’s talk stress free examinations. See you on 1st April at Pariksha Pe Charcha."))
# print(readability_score("")

final_df['read_score'] = ""
for i in range(0,len(final_df)):
    final_df['read_score'][i] = readability_score(final_df['Text'][i])
    
# final_df['Party'] = "" 
# for i in range(0,101):  
#     final_df['Party'][i] = "BJP"
# for i in range(101,365):  
#     final_df['Party'][i] = "SP"
# for i in range(365,466):  
#     final_df['Party'][i] = "INC"
# for i in range(466,668):  
#     final_df['Party'][i] = "BJP"
    

sns.distplot(final_df[final_df['Party']=='BJP'].read_score, label = 'BJP')
sns.distplot(final_df[final_df['Party']=='INC'].read_score, label = 'INC')
plt.title('ARI score of republican vs democrats')
plt.legend()
plt.legend()
plt.xlim(-10,25)

from wordcloud import WordCloud, STOPWORDS , ImageColorGenerator
#%matplotlib inline

politican = ['narendramodi']
plot = []
stopwords = set(STOPWORDS)
for idx, name in enumerate(politican):
    politican_df = final_df[final_df['Username'] == name] 
    politican_df_tweet = " ".join(review for review in politican_df.Text)
    wordcloud = WordCloud(max_font_size=50, max_words=100, stopwords=stopwords, background_color="white").generate(politican_df_tweet)
    plt.imshow(wordcloud)
    # plot.append(wordcloud)
 
# fig, axs = plt.subplots(4, 2 , figsize  = (30,30))

# for i in range(4):
#     for j in range(2):
#         if i == 3 and j == 2: 
#             break 
#         axs[i,j].imshow(plot[i*2+j], interpolation='bilinear')
#         axs[i,j].axis("off")
#         axs[i,j].set_title('Most common words used by: ' +politican[i*2+j],fontsize=30)
#         #axs[i,j].show()
# plt.savefig(one_level_up + '\\report_graph\\WC_woCommon')
# old_df = pd.read_csv("old_tweets.csv")

# for i in old_df['Text']:
#     print(i)
#     break
    