import tweepy

import os


def TweepyAuth():
    token = os.environ.get('TWITTER_API_ACCESS_TOKEN')
    token_secret = os.environ.get('TWITTER_API_ACCESS_TOKEN_SECRET')

    consumer_key = os.environ.get('TWITTER_API_KEY')
    consumer_secret = os.environ.get('TWITTER_API_SECRET')

    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(token, token_secret)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
        print("Authentication Successful")
        return api
    except BaseException:
        print("Authentication Error")
        return None


# Create a new instance of the api wrapper.
api = TweepyAuth()

# Return the authenticated User.
me = api.me()

# Create a new status and fetch the timeline.
api.update_status("this is a test tweet")
s = api.user_timeline(me.id)

print(s)
