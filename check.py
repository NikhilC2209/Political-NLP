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
import os
from dotenv import load_dotenv

load_dotenv()

# assign the values accordingly
consumer_key = os.getenv("API_Key")
consumer_secret = os.getenv("API_Key_Secret")
access_token = os.getenv("Access_Token")
access_token_secret = os.getenv("Access_Token_Secret")
  
# authorization of consumer key and consumer secret
auth = tweepy.OAuthHandler(consumer_key, consumer_secret, access_token, access_token_secret)
  
# set access to user's access key and access secret 
# auth.set_access_token(access_token, access_token_secret)

# calling the api 
api = tweepy.API(auth)

# fetching the verified user
#user = api.verify_credentials()

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")

# query = '@narendramodi'
# max_tweets = 10
# tweets = [status for status in tweepy.Cursor(api.search_tweets, q=query).items(max_tweets)]

# print(tweets)

#print("The user has " + str(user.followers_count) + " followers.")
#print("The user has " + str(user.friends_count) + " friends.")