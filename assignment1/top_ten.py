#################################################################
# Name: Junzhi Ye 
# Coursera Intro to Data Science Assignment 1 
# Description: Computes the top ten most frequently occurring 
# hashtags 
#
# Execution: 
# % python top_ten.py tweet_file.txt
#################################################################

import sys
import json
import twitter

# get the unique items
def getUnique(seq):
    seen = set()
    seen_add = seen.add
    return [x for x in seq if not (x in seen or seen_add(x))]

# program runs 
def main():
    
    # tweets
    tweet_file = open(sys.argv[1])

    # add each tweet to tweets
    tweets = []
    for line in tweet_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass
    
    # every hashtag that occurs in the tweets
    all_hashtags = []
    # for every tweet
    for tweet in tweets:
        if 'entities' in tweet:
            # number of hashtag fields(?) in the tweet
            length = len(tweet['entities']['hashtags'])
            # get all of the hashtags
            for i in range(length):
                all_hashtags.append(tweet['entities']['hashtags'][i]['text'])
    
    # get the unique hashtags         
    unique_hashtags = getUnique(all_hashtags)

    # count the number of occurrences of each unique hashtag in 
    # the list of all hashtags
    # print each hashtag and its number of occurrences
    for i in range(len(unique_hashtags)):
        print unique_hashtags[i], all_hashtags.count(unique_hashtags[i])

if __name__ == '__main__':
    main()
