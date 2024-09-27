# import snscrape.modules.twitter as sntwitter
# import pandas as pd

# query = "from:elonmusk"
# max_tweets = 10

# tweets_list = []

# for i, tweet in enumerate(sntwitter.TwitterSearchScraper(query).get_items()):
#     if i >= max_tweets:
#         break
#     tweets_list.append([tweet.date, tweet.id, tweet.content, tweet.username, tweet.likeCount, tweet.retweetCount])

# tweets_df = pd.DataFrame(tweets_list, columns=["Date", "Tweet ID", "Content", "Username", "Likes", "Retweets"])

# print(tweets_df.head())

import tweepy

# Your Twitter API credentials
api_key = 'eWUewtZyYOGNCA4mtguD3YULx'
api_secret_key = 'f2zFBAtlW1dHB775secADMnl1UdkykeBDOOh4hzC8xAxHb0jlV'
access_token = '1730529935763374080-4Nt4bzPQBveBCtETDuUh9c41SEzXtw'
access_token_secret = 'QSshP4MTrPesY1hjl9OS5cbadkW8bquafNdQ5pYLgjYVj'

# Authenticate with the Twitter API
auth = tweepy.OAuthHandler(api_key, api_secret_key)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# Get trending topics for a specific location (WOEID)
# WOEID for Worldwide: 1, for the USA: 23424977, for India: 23424848
woeid = 1 

# Fetch the trending topics
trending_topics = api.get_place_trends(woeid)

# Display the top trending topics
for trend in trending_topics[0]["trends"]:
    print(trend["name"])