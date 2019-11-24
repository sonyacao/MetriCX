"""
Sonya Cao, Janice Xu, Shirley Wu
11/23/19
Sentiment Analysis: program used to analyze Twitter tweets for a business and output a personalised response
"""

infile = open("responses.txt", encoding='utf‐8', errors='ignore')

dictionary = {}
valid = False
for line in infile:
    value = line.split("|")
    response = value[1]
    word = value[0]
    dictionary[word] = response

data = input("Please input a tweet in here").split("|")
while valid ==False:
    if len(data) == 4:
        valid == True
        break
    else:
        data = input("Invalid format. Please try inputting a tweet again").split("|")

user = data[2]
tweet = data[3]
responded = False

for word in dictionary:
    if word in tweet:
        print("Dear {}".format(user) + ", " +dictionary[word])
        responded =True
        break

if responded == False:
    print("Dear {}, please call us at 1 800 957 9777".format(user))
