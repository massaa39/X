import get_twitter
import bot_twitter

tweet_content = get_twitter.make_tweet()
if tweet_content:
    bot_twitter.post_tweet(tweet_content)
else:
    print("Failed to generate tweet content.")

