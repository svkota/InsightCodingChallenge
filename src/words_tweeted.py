# example of program that calculates the total number of times each word has been tweeted.

import numpy as np

# read text file
file = open('tweet_input/tweets.txt','r')
#print(file)

allWords = np.empty(shape=(0,0))
#print(allWords)

# write words in a text file to single array
for line in file:
   # read words in each line
   words = line.split();
   # append words from each line into one array
   allWords = np.append(allWords, words);                 
file.close()

# find unique words in a text file, unique also sorts so need to sort
uniqueWords = np.unique(allWords)

#print('Number of words in a text file',len(allWords))
#print('Number of unique words in a text file',len(uniqueWords))


# find the total number of number of times each words has been tweeted
# create an array with length of uniquewords to save number of times each word has been tweeted
wordCount = np.zeros((len(uniqueWords),), dtype= np.int)
for x in range(0, len(uniqueWords)):
    wordCount[x] = list(allWords).count(uniqueWords[x])

# stack unique words and number of times they were tweeted
wordsAndCount = np.column_stack([uniqueWords, wordCount])

# save data into a text file
np.savetxt('tweet_output/ft1.txt', wordsAndCount, fmt='%+s',  delimiter='\t')

