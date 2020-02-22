# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 12:41:10 2020

@author: manis
"""
import time
start_time = time.time()

from math import sqrt
from itertools import permutations

def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True


lst=[''.join(p) for p in permutations("1234567")]

for i in reversed(lst):
    if isPrime(int(i)):
        print(i)
        break
print("Program run time(in s): ", (time.time() - start_time))
