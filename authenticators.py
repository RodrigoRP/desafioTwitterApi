import dotenv
import os
import tweepy


def get_credential_api():
    dotenv.load_dotenv(dotenv.find_dotenv())

    access_token_secret = os.getenv("access_token_secret")
    consumer_secret = os.getenv("consumer_secret")
    access_token = os.getenv("access_token")
    consumer_key = os.getenv("consumer_key")

    authenticate = tweepy.OAuthHandler(consumer_key, consumer_secret)
    authenticate.set_access_token(access_token, access_token_secret)

    return tweepy.API(authenticate, wait_on_rate_limit=True)


def authentication_db():
    dotenv.load_dotenv(dotenv.find_dotenv())

    param_dic = {
        "host": os.getenv("host"),
        "database": os.getenv("dbname"),
        "user": os.getenv("user"),
        "password": os.getenv("password")
    }

    return param_dic
