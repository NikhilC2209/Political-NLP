import os
import pandas as pd
import numpy as np
from dotenv import load_dotenv
import tweepy
from deep_translator import GoogleTranslator
load_dotenv()

API_KEY = os.getenv('API_Key')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
BEARER_TOKEN = os.getenv('Bearer_Token')
ACCESS_TOKEN = os.getenv('Access_Token')
ACCESS_TOKEN_SECRET = os.getenv('Access_Token_Secret')

auth = tweepy.auth.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

query = '@narendramodi since:2022-02-01 until:2022-03-15'
#query = '#UPElections2022 since:2022-01-01 until:2022-03-30'
#query = '@yadavakhilesh'	#SP
#query = '@priyankagandhi'	#INC
#query = '@AmitShah'		#BJP
#query = '@MamataOfficial'	
#query = '@myogiadityanath'	#BJP
#query = '@JM_Scindia'
#query = '@SwamiPMaurya'	#SP
#query = '@shivpalsinghyad'	#SP
#query = '@AjayLalluINC'	#INC
#query = '@kpmaurya1'	#BJP
#query = '@ptshrikant'	#BJP


max_tweets = 1000
#since_date = '2022-02-01'
#until_date = '2022-03-10'
tweets = [status for status in tweepy.Cursor(api.search_tweets, q=query).items(max_tweets)]
#tweets = [status for status in tweepy.Cursor(api.user_timeline, screen_name=query).items(max_tweets)]

#print(tweets[0])

# def pre_process():

columns = ['User', "Tweet", 'Date','Location', 'Language']
data = []

# txt = "It was special to be at the Orakandi Thakurbari in Bangladesh in March 2021. Here is my speech during that programmâ€¦ https://t.co/kP6aiFu8jQ"
# txt = txt.split(" ")
# if "#UPElections2022"in txt:
# 	print("dfsdfd")
#print(txt.text.find(""))

# for i in tweets:
# 	#print(i.user.screen_name)
# 	# temp = i.text.split(" ")
# 	# if "#UPElection2022" in temp:
# 		if(i.lang=='hi'):
# 			i.text = GoogleTranslator(source='auto', target='en').translate(i.text)
# 		data.append([i.user.screen_name, i.text, i.created_at, i.user.location, i.lang])

for i in tweets:
	if(i.lang=='hi'):
		i.text = GoogleTranslator(source='auto', target='en').translate(i.text)
	data.append([i.user.screen_name, i.text, i.created_at, i.user.location, i.lang]) 

#print(data)

df = pd.DataFrame(data, columns=columns)
#print(df)
df.to_csv("tweets.csv")
