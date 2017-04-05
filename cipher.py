
# coding: utf-8

# In[ ]:

def takeInput():
    while(True):
        m = int(raw_input('Enter lower bound m: '))
        if m > 0 and m < 676:
            break
    while(True):
        n = int(raw_input('Enter upper bound n: '))
        if n > m and n < 676:
            break
    return [m ,n]


# In[ ]:

def decoder(num):
    if num > 26:
        second = num%26
        if second == 0:
            first = num/26 - 1
            second = 26
        else:
            first = num/26
        return chr(first+64) + chr(second+64)
    else:
        first = num%27
        return chr(first + 64)


# In[ ]:

result = []
if __name__ == "__main__":
    m, n = takeInput()
    for i in range(m,n+1):
        result.append(decoder(i))
        print result[len(result) - 1]

