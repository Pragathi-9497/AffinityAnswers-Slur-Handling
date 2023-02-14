#!/usr/bin/env python
# coding: utf-8

# Imagine there is a file full of Twitter tweets by various users and you are provided a set of words that indicates racial slurs. Write a program that can indicate the degree of profanity for each sentence in the file. Write in any programming language (preferably in Python) 

# In[11]:


import re

slurs = ['slur-1', 'slur-2', 'slur-3', "slur-4"...]    #List of racial slurs 

def profanity_score(tweet): # Function for calculating the profanity score  
    tweet_lower = tweet.lower() # To overcome case-insensitivity, tweets are converted to lowercase
    slur_count = len(re.findall('|'.join(slurs), tweet_lower)) # To count the number of slurs in the tweet
    score = slur_count / len(tweet) if len(tweet) > 0 else 0 # Formula-> Profinity score=  number of slurs/length of the tweet
    return profanity_score

file_path = 'path/to/tweets/file.txt' # path of tweet file
with open(file_path, 'r') as tweets_file: # Open and read the tweets in the file
    tweets = tweets_file.readlines()

for tweet in tweets: #Calculating the profanity score for each tweet 
    score = profanity_score(tweet)
    print(f'Tweet: {tweet.strip()} | Profanity score: {profanity_score}')

