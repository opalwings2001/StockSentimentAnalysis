import pandas as pd
from pandas.io.json import json_normalize
import requests
import tweepy
import json
import config


# Things to install: tweepy, nltk, pandas, flask, wordcloud

def make_query(symbol):
    from datetime import date

    query = f"{symbol} -is:retweet"
    client = tweepy.Client(bearer_token=config.bearer_token, return_type=requests.Response)

    # To set today's date start time
    today = date.today()
    date = today.strftime("%Y-%m-%d")
    starttime = date + "T00:00:00Z"

    # To get the tweets
    response = client.search_recent_tweets(query=query, max_results=100, start_time=starttime, tweet_fields=['created_at', 'lang'])

    # To get volume of tweets
    tweet_count = client.get_recent_tweets_count(query=query)

    # for count in tweet_count:
    #     print(count)

    tweets_dict= response.json()
    tweets_data = tweets_dict['data']
    #type(tweets_data)
    df = pd.json_normalize(tweets_data)

    df.to_csv("hackhers_sample2.csv")
    print(df.head())
    return df










