#################################################################
# Name: Junzhi Ye 
# Coursera Intro to Data Science Assignment 1 
# Description: Compute the term frequency histogram of the 
# livestream data 
#
# Execution: 
# % python frequency.py tweet_file.txt
#################################################################

import sys
import json

# unique items 
def getUnique(seq):
    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

# program begins
def main():
    
    # tweets
    tweet_file = open(sys.argv[1])
    # read in all tweets 
    all_tweets = tweet_file.readlines()
    
    # all tokens (words) that occur in every tweet
    alltokens = []
    # total number of tokens in all tweets 
    total = 0

    # for each tweet 
    for line in all_tweets:
        # if the tweet has valid text 
        if json.loads(line).has_key('text'):
            # get the text of the tweet
            tweettext = json.loads(line).get('text').encode('UTF-8')
            # tokens of the tweet's text
            tokens = tweettext.split()
            # add each token of the tweet's text to alltokens
            for token in tokens:
                alltokens.append(token)
                # increment the total number of tokens 
                total += 1

    # get the unique tokens 
    uniquetokens = getUnique(alltokens)

    # for each unique token 
    for i in range(len(uniquetokens)): 
        # output contains a term, followed by a space, followed 
        # by the frequency of that term in the entire file 
        print uniquetokens[i], alltokens.count(uniquetokens[i])/total

if __name__ == '__main__':
    main()
