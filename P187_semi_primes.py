# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:52:02 2020

@author: Manish
"""

import sympy
import time


def Q187():
    n = 10**8
    counter = 0
    plist = list(sympy.sieve.primerange(0, n//2 + 1))
    for i in range(len(plist)):
        for j in range(i, len(plist)):
            if plist[i]*plist[j] > n:
                break
            counter += 1
    print(counter)


if __name__ == '__main__':
    start_time = time.time()
    Q187()
    print("Program run time(in s): ", (time.time() - start_time))