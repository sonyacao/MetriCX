from sentiment_analysis import compute_tweets

tweets = input("Please enter the name of the tweets file")
poskey = input("Please enter the name of the positive keywords file")
negkey = input("Please enter the name of the negative keywords file")
results = compute_tweets(tweets, poskey, negkey) #calling the compute function to find the results for each region

print("Total positive tweets is ", results[0], "and total negative tweets is ", results[1], "out of ", results[2], "total tweets" )
print("The overall score is ", results[3])
