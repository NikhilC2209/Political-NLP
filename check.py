# import os
# import pandas as pd
# import numpy as np
# from dotenv import load_dotenv
# import tweepy
# from deep_translator import GoogleTranslator
# load_dotenv()

# API_KEY = os.getenv('API_Key')
# API_KEY_SECRET = os.getenv('API_KEY_SECRET')
# BEARER_TOKEN = os.getenv('Bearer_Token')
# ACCESS_TOKEN = os.getenv('Access_Token')
# ACCESS_TOKEN_SECRET = os.getenv('Access_Token_Secret')

# auth = tweepy.auth.OAuthHandler(API_KEY, API_KEY_SECRET)
# auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
# api = tweepy.API(auth)

# if(api.verify_credentials()==False):
# 	print("the user credentials are invalid")
# else:
# 	print("Valid")

import tweepy
  
# assign the values accordingly
consumer_key = "SXsNHkozdO4yHov4QzhGSExTr"
consumer_secret = "Opt4HV9BgfEnOaUWe3QoK6SJ0g635LzCZ75TqR89QoNq72Q8D0"
access_token = "903688502524616705-EkszvpQyi8BczMFT8Wqm43tE1h7AXlu"
access_token_secret = "Ucf9qX52WuOiyNsmIqKTM6DK70tA37XGu41N5zkaXp4kx"
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
  
# set access to user's access key and access secret 
# auth.set_access_token(access_token, access_token_secret)

# calling the api 
api = tweepy.API(auth)

# fetching the verified user
#user = api.verify_credentials()

query = '@narendramodi'
max_tweets = 10
tweets = [status for status in tweepy.Cursor(api.search_tweets, q=query).items(max_tweets)]

print(tweets)

#print("The user has " + str(user.followers_count) + " followers.")
#print("The user has " + str(user.friends_count) + " friends.")