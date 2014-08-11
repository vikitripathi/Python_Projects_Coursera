#################################################################
# Name: Junzhi Ye 
# Coursera Intro to Data Science Assignment 1 
# Description: Returns the name of the happiest state as a string
#
# Execution: 
# % python happiest_state.py sentiment_file.txt tweet_file.txt
#################################################################

import sys
import json 
import twitter

# get the unique items in a list(?) 
def getUnique(seq):

    seen = set()
    seen_add = seen.add
    return [ x for x in seq if not (x in seen or seen_add(x))]

def main():
    
    # sentiments file with sentiment key and score 
    sent_file = open(sys.argv[1])
    # tweets
    tweet_file = open(sys.argv[2])

    # make a dictionary from key-integer pairs in the
    # sentiment file 
    scores = {}
    for line in sent_file:
        term, score = line.split("\t") 
        scores[term] = int(score)
    
    # append each tweet to tweets 
    tweets = []
    for line in tweet_file:
        try:
            tweets.append(json.loads(line))
        except:
            pass

    # states with number of occurrences corresponding 
    # to total sentiment score of tokens whose tweets are
    # in that state 
    results = []
    for tweet in tweets:
        if 'user' in tweet:
            # location string of the tweet
            location = tweet['user']['location']
            # words in the location string 
            location_tokens = location.split()
            # tokens in the location string 

            for tl in location_tokens:
                # if a token corresponds to a two letter
                # state abbreviation as defined in states
                if tl in states:
                    # the text of the tweet
                    text = tweet.get('text').encode('UTF-8')
                    # the words in the tweet text
                    text_tokens = text.split()

                    # calculate the tweet's sentiment score
                    # initialize the sentiment score of the tweet 
                    t = 0
                    # for each token in the tweet text 
                    for tt in text_tokens:
                        # sentiment score for that token 
                        if tt in scores:
                            t += scores[tt] 
                    # add the state abbreviation the number of times
                    # corresponding to the sentiment score of this 
                    # tweet 
                    for i in range(0, t):
                        results.append(tl)
    
    # get the unique states 
    uniqueresults = getUnique(results)

    max = 0 
    # count the number of occurences of each unique state in the results
    # the state with the max number of occurences is the happiest state
    for i in range(len(uniqueresults)): 
        count = results.count(uniqueresults[i])
        if count > max:
            max = count 
            happiest_state = uniqueresults[i]

    print happiest_state

# dictionary of state abbreviations 
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
  
if __name__ == '__main__':
    main()
