
# coding: utf-8

# In[ ]:

import numpy as np

def takeInput(data, lenCounts):
    i = 1
    while(True):
        d = raw_input('Input ' + str(i) + ": ")
        ## exit taking input on enocuntering string "end"
        if d.lower() == "end":
            return 
        ## length of input strinf must be greater than 0
        elif len(d) != 0:
            data.append(d)
            lenCounts.append(len(d))
            i = i + 1

sortedData = [] # list for string sequence after sorting
if __name__ == "__main__":
    data = []
    lenCounts = []
    print 'Type end after last string input.'
    takeInput(data, lenCounts)
    sortedIndex = np.argsort(lenCounts)
    for i in range(len(lenCounts)):
        sortedData.append(data[sortedIndex[i]])
        print data[sortedIndex[i]]

