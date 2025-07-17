import tweepy as tw
import constants

auth = tw.OAuthHandler(constants.TWITTER_API_KEY, constants.TWITTER_API_SECRET)
auth.set_access_token(constants.TWITTER_ACCESS_TOKEN, constants.TWITTER_ACCESS_SECRET)
api = tw.API(auth, wait_on_rate_limit=True)

client = tw.Client(
    bearer_token=constants.BEARER_TOKEN,
    consumer_key=constants.TWITTER_API_KEY,
    consumer_secret=constants.TWITTER_API_SECRET,
    access_token=constants.TWITTER_ACCESS_TOKEN,
    access_token_secret=constants.TWITTER_ACCESS_SECRET,
    wait_on_rate_limit=True
)

query = client.search_recent_tweets(query = "stopkillinggames", max_results=10)
# tweets = [{"Tweets": tweet.text, "Timestamp":tweet.created_at} for tweet in query]
if query.data:
    for tweet in query.data:
        print(tweet.text)
else:
    print("no response :c")