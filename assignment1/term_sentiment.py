#################################################################
# Name: Junzhi Ye 
# Coursera Intro to Data Science Assignment 1 
# Description: Derive the sentiment of new terms that do not
# appear in the sentiments file
#
# Execution: 
# % python term_sentiment.py sentiment_file.txt tweet_file.txt
#################################################################

import sys
import json

# program begins 
def main():

    # file with key value sentiment pairs
    sent_file = open(sys.argv[1])
    # file with tweets 
    tweet_file = open(sys.argv[2])

    # create a dictionary of sentiments
    scores = {}
    for line in sent_file:
        term, score = line.split("\t")
        scores[term] = int(score)

    # preserve the original sentiments dictionary 
    newdict = scores.copy()

    # for every line in the tweets file 
    for line in tweet_file:
        # if the line has valid tweet text 
        if json.loads(line).has_key('text'):

            # get the text of the tweet
            tweettext = json.loads(line).get('text').encode('UTF-8')
            # convert tweet into a list of tokens 
            tokens = tweettext.split()

            # find the tweet's sentiment
            sentiment = 0
            # for each token of the tweet
            for token in tokens:
                # if the token is in the sentiment dictionary
                if token in scores:
                    # add the token's sentiment score to the tweet's
                    # sentiment
                    sentiment += scores[token] 
            # go through the tweet's token's again to 
            # add new tokens to scores 
            for token in tokens:
                # if the token was not in the original sentiments
                if token not in newdict:
                    # if the sentiment score for this tweet > 0
                    if sentiment > 0:
                        scores[token] = 1.0
                    else:
                        scores[token] = 0.0

    # print the additions to the sentiments dictionary to stdout
    # a term, followed by a space, followed by the sentiment
    for term in scores:
        if term not in newdict:
            print term, float(scores[term])

if __name__ == '__main__':
    main()
