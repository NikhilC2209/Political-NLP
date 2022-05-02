import os
from dotenv import load_dotenv
import tweepy
load_dotenv()

API_KEY = os.getenv('API_Key')
API_KEY_SECRET = os.getenv('API_KEY_SECRET')
BEARER_TOKEN = os.getenv('Bearer_Token')
ACCESS_TOKEN = os.getenv('Access_Token')
ACCESS_TOKEN_SECRET = os.getenv('Access_Token_Secret')

# auth = tweepy.OAuthHandler(API_KEY, API_KEY_SECRET)
# auth.set_access_token(ACESS_TOKEN, ACCESS_TOKEN_SECRET)

# api = tweepy.API(auth)

# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print(tweet.text)

auth = tweepy.auth.OAuthHandler(API_KEY, API_KEY_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

query = '#UPElections'
max_tweets = 10
searched_tweets = [status for status in tweepy.Cursor(api.search_tweets, q=query).items(max_tweets)]

print(searched_tweets[1].text)

#for i in searched_tweets:
 #   print(i)



# print(BEARER_TOKEN)

# client = tweepy.Client(BEARER_TOKEN, wait_on_rate_limit=True)

# response = client.get_all_tweets(
#                 "Tweepy",
#                 query = 'COVID -is:retweet lang:en',
#                 tweet_fields=["created_at", "lang"]
# )
# tweets = response.data

# print(tweets[43])

# print(os.getenv('API_Key'))