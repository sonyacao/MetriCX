from string import punctuation

def compute_tweets(tweets, poskey, negkey):  # function to determine the current customer happiness score of a business based on their mentioned tweets

    try:
        t = open(tweets, encoding='utf‐8', errors='ignore')
    except IOError:
        print('Tweets file does not exist')
        t.close()
        return []

    positive = positivelist(poskey)#list of all words associated with a positive opinion
    negative = negativelist(negkey)  #list of all words associated with a negative opinion
    totalpos = 0
    totalneg = 0
    totalsenti = 0
    totaltweets = 0

    line = t.readline()
    while line != "": #will continue to loop until the end of the file is reached
        sentiment = sentiment_calc(line, positive, negative)
        if sentiment == 1:
            totalpos +=1
            totalsenti +=1
        elif sentiment == -1:
            totalneg +=1
            totalsenti -= 1
        totaltweets += 1
        line = t.readline()
    t.close()

    score = totalsenti/totaltweets

    return [totalpos, totalneg, totaltweets, score]

def positivelist(poskey):
    positive =[]
    try:
        p = open(poskey, encoding='utf‐8', errors='ignore')
    except IOError:
        print('Positive keywords file does not exist')
        p.close()
        return []
    line = p.readline()
    while line != "":  # will continue to loop until the end of the file is reached
        positive.append(line.strip())
        line = p.readline()
    p.close()

    return positive

def negativelist(negkey):
    negative = []
    try:
        n = open(negkey, encoding='utf‐8', errors='ignore')
    except IOError:
        print('Negative keywords file does not exist')
        n.close()
        return []
    line = n.readline()
    while line != "":  # will continue to loop until the end of the file is reached
        negative.append(line.strip())
        line = n.readline()
    n.close()

    return negative

def sentiment_calc(line, positive, negative):
    senti = 0  # variable that stores the sum of the sentiment value of the keywords mentioned in the tweet
    data = line.split("|")  # creating a list of the words in the tweet
    words = data[3].split()

    for word in words:  # looping through each word in the tweet
        word = word.strip(punctuation)  # removing all punctuation from the beginning and end of each word in the tweet
        # if the word is in one of the keys in the dictionary, total key and total sentiment are updated
        word = word.lower()
        if word in positive:
            senti += 1
        if word in negative:
            senti += -1

    if senti > 0:
        return 1
    elif senti < 0:
        return -1
    else:
        return 0





