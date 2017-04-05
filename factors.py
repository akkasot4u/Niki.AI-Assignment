
# coding: utf-8

# In[ ]:

import numpy as np


# In[ ]:

def primeFactors(num):
    factors = []
    if num%2 == 0:
        factors.append(2)
    if num%3 == 0:
        factors.append(3)
    sqrtNum = int(num**(1/2.0))
    ## find remaining prime factors
    for k in range(1, sqrtNum+1):
        m = 6*k - 1
        n = 6*k + 1
        if num%m == 0:
            factors.append(m)
        if num%n == 0:
            factors.append(n)
    return factors


# In[ ]:

def allFactors(num):
    factors = []
    sqrtNum = int(num**(1/2.0))
    for k in range(1, sqrtNum+1):
        if num%k == 0:
            factors.append(k)
            factors.append(num/k)
    if factors[len(factors) - 1] == factors[len(factors) - 2]:
        factors.pop()
    return np.sort(factors)


# In[ ]:

if __name__ == "__main__":
    num = int(raw_input("Enter number to factorise: "))
    factors = allFactors(num)
    primes = primeFactors(num)
    if len(factors) == 1:
        print str(num) + 'is a prime number.'
    print 'All factors of ' + str(num) + ' are:'
    for i in factors:
        print i
    print 'Prime factors of '+ str(num) + ' are:'
    for i in primes:
        print i

