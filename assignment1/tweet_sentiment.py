#################################################################
# Name: Junzhi Ye 
# Coursera Intro to Data Science Assignment 1 
# Description: Compute the sentiment of each tweet based on the
# sentiment scores of the terms in the tweet. 
#
# Execution: 
# % python tweet_sentiment.py sentiment_file.txt tweet_file.txt
#################################################################

import sys
import json

# begin
def main():

    # sentiments file
    sent_file = open(sys.argv[1])
    # tweets file
    tweet_file = open(sys.argv[2])

    # make a dictionary from key integer pairs in the
    # sentiment file 
    scores = {}
    for line in sent_file:
        term, score = line.split("\t") 
        scores[term] = int(score)

    # for every line in the tweets file
    for line in tweet_file:
        # if the line has valid tweet text 
        if json.loads(line).has_key('text'):
            # get the text of the tweet
            tweettext = json.loads(line).get('text').encode('UTF-8')
            # convert the text of the tweet into a list of tokens 
            tokens = tweettext.split()
            # calculate the tweet's sentiment score
            sentiment = 0
            # for each token in the tweet text 
            for token in tokens:
                # if the token is in the sentiments dictionary
                if token in scores:
                    # add the sentiment of the token to the tweet's
                    # sentiment score 
                    sentiment += scores[token]
                # print to stdout the sentiment of each tweet in the
                # file, one numeric sentiment per line
                print sentiment
        
if __name__ == '__main__':
    main()
