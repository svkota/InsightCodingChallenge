# example of program that calculates the median number of unique words per tweet.

import numpy as np

# count number of lines in the text
line_count = sum(1 for line in open('tweet_input/tweets.txt','r'))
#print('Number of lines in the text are ', line_count)

# initialize arrays
numberOfUniqueWords = np.zeros((line_count,), dtype = np.int)
medianOfUniqueWords = np.zeros((line_count,), dtype = np.float)

# read text file
file = open('tweet_input/tweets.txt','r')


k = 1#variable to increase

for line in file:
   #print(line)
   words = line.split();
   numberOfWords = len(words)
   #print('Number of words in the sentence ', k , ':', numberOfWords)

   # find number of unique words
   numberOfUniqueWords[k-1] = len(np.unique(words))

   #median of unique words
   medianOfUniqueWords[k-1] = np.median(numberOfUniqueWords[0:k])

   k = k + 1                  
file.close()


np.savetxt('tweet_output/ft2.txt', medianOfUniqueWords, fmt='%.2f')
