# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

#################### by khyatee desai

import tweepy
from textblob import TextBlob

# access token and keys/secrets go here:


auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)

term =input("Enter a term you would like to search on twitter: ")
public_tweets = api.search(term)

pol=[]
subj=[]

print("Tweets for search term:", term,'\n')
for tweet in public_tweets:
	print(tweet.text)
	analysis = TextBlob(tweet.text)
	pol.append(analysis.sentiment.polarity)
	subj.append(analysis.sentiment.subjectivity)
	print('\n========================================================================\n')
summ=0
for i in pol:
    summ +=i
avpol= summ/len(pol)

for i in subj:
	summ +=i
avsubj = summ/len(subj)


print("Average subjectivity is", avpol)
print("Average polarity is", avsubj)
