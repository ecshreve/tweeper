import tweepy
import os
import logging

logger = logging.getLogger()


def create_api():
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
    except Exception as e:
        logger.error("Error creating API", exc_info=True)
        raise e

    logger.info("API Created Successfully")
    return api
