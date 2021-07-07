import tweepy

from authenticators import get_credential_api


def get_list_tweets(search_words):
    api = get_credential_api()

    tweets = tweepy.Cursor(api.search,
                           q=str(search_words) + "-filter:retweets",
                           lang='pt',
                           result_type="recent").items(50)

    return [[tweet.user.screen_name, tweet.user.location, tweet.text] for tweet in tweets]
