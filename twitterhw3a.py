# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.
import tweepy
import json

# access token and keys/secrets


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)


api = tweepy.API(auth)
api.update_with_media('b9055a17eada7348920c3190c482d058.jpg')

