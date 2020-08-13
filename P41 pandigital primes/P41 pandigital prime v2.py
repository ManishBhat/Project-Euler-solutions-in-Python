# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:41:10 2020

@author: manis
"""

import time
from math import sqrt
from itertools import permutations

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True

def Q41():
    lst=[''.join(p) for p in permutations("1234567")]
    # Note 5,6, 8 digit and 9 digit pandigital primes aren't possible as 
    # the sum of digits is divisible by 3. Thus, we only have to test 7 digit
    # pandigital numbers
    for i in reversed(lst):
        if isPrime(int(i)):
            print(i)
            break
        
if __name__ == "__main__":
    start_time = time.time()
    Q41()
    print("Program run time(in s): ", (time.time() - start_time))
