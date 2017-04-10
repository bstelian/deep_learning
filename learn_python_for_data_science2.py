import tweepy
from textblob import TextBlob

# Step 1 - Authenticate
consumer_key= 'RwCohzkYZ4WicSbnlh0pd9sMU'
consumer_secret= 'qkATXyQf6rUGWHIFGB9f0Q9rHvn6YGALcDzFL8bJHPcDGHdU69'

access_token='849333564655239168-EdsSJhfNSLn82KFNnFXkvkDkM9RZmIw'
access_token_secret='6nnrErppAAaTqMGVeERoPzPnlfArGuLrMkEKdvOkAgyob'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

#Step 3 - Retrieve Tweets
public_tweets = api.search('Trump')



#CHALLENGE - Instead of printing out each tweet, save each Tweet to a CSV file
#and label each one as either 'positive' or 'negative', depending on the sentiment 
#You can decide the sentiment polarity threshold yourself


for tweet in public_tweets:
    print(tweet.text)
    
    #Step 4 Perform Sentiment Analysis on Tweets
    analysis = TextBlob(tweet.text)
    print(analysis.sentiment)
    print("")
