import os
import tweepy

# 環境変数からTwitter APIキーを取得する
consumer_key = os.getenv("TWITTER_CONSUMER_KEY")
consumer_secret = os.getenv("TWITTER_CONSUMER_SECRET")
access_token = os.getenv("TWITTER_ACCESS_TOKEN")
access_token_secret = os.getenv("TWITTER_ACCESS_TOKEN_SECRET")
bearer_token = os.getenv("TWITTER_BEARER_TOKEN")

# tweepyクライアントの設定
client = tweepy.Client(
    bearer_token=bearer_token,
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret
)

def post_tweet(tweet):
    try:
        response = client.create_tweet(text=tweet)
        print(f"Tweeted: {tweet}")
        return response
    except tweepy.TweepyException as e:
        print(f"Twitter API Error: {e}")
        return None
