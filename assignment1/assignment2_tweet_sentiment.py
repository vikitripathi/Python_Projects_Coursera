import sys
import json

scores = {} # initialize an empty dictionary
	
def readSentimentFile(afinnfile):
	for line in afinnfile:
                #multiple assignment by using list
		term, score  = line.split("\t") #the file is tab-delimited."\t" means "tab character"
		scores[term] = int(score) #Convert the score to an integer.

def deriveSentimentOfTweets(json_data):
	reload(sys)
	sys.setdefaultencoding("utf8")
	for line in json_data:
		sentiment = 0
		data = json.loads(line)
		tweet = str(data.get("text"))
		#use get function in data dictionary for the key text
		words = tweet.split(' ')
		for word in words:
			if word in scores:
				sentiment += scores[word]	
		print(str(sentiment))
	json_data.close()

def main():
	sentiment_file = open(sys.argv[1])
	tweet_file = open(sys.argv[2])
	readSentimentFile(sentiment_file)
	deriveSentimentOfTweets(tweet_file)

if __name__ == '__main__':
	main()

