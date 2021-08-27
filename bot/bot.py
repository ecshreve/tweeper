import tweepy

import os

token = os.environ.get('TWITTER_API_ACCESS_TOKEN')
token_secret = os.environ.get('TWITTER_API_ACCESS_TOKEN_SECRET')

key = os.environ.get('TWITTER_API_KEY')
key_secret = os.environ.get('TWITTER_API_SECRET')

# Authenticate to Twitter
auth = tweepy.OAuthHandler(token, token_secret)
auth.set_access_token(key, key_secret)
api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication Successful")
except BaseException:
    print("Authentication Error")
