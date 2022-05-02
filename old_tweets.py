import snscrape.modules.twitter as sntwitter
import pandas as pd
from deep_translator import GoogleTranslator

tweets_df = pd.read_csv("old_tweets.csv")

# Creating list to append tweet data to
tweets_list2 = []

# Using TwitterSearchScraper to scrape data and append tweets to list
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:@ptshrikant since:2022-02-01 until:2022-04-15').get_items()):
    if i>100:
        break
    if(tweet.lang=='en'):    
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    else:
        tweet.content = GoogleTranslator(source='auto', target='en').translate(tweet.content)
        tweets_list2.append([tweet.date, tweet.id, tweet.content, tweet.user.username])
    
# Creating a dataframe from the tweets list above
tweets_df2 = pd.DataFrame(tweets_list2, columns=['Datetime', 'Tweet Id', 'Text', 'Username'])

frames = [tweets_df, tweets_df2]
tweets_final = pd.concat(frames)
tweets_final.to_csv("old_tweets.csv")