# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 05:12:34 2020

@author: manis
"""

import time

def collatz(n,collatz_dict):
    if collatz_dict.get(n) is None:    
        if n % 2 == 0:
            collatz_dict[n] = collatz(n/2, collatz_dict) + 1   
        else:
            collatz_dict[n] = collatz(3*n+1, collatz_dict) + 1 
    return collatz_dict[n]


def main():
    N = 1_000_000
    collatz_dict = {}
    collatz_dict[1] = 1
    maxcollatz = n = 11
    maxn = 1
    for n in range(1, N):
        x = collatz(n, collatz_dict)
        if x > maxcollatz:
            maxcollatz = x
            maxn = n
    print("Number with largest collatz sequence: ",maxn)
    print("Sequence length: ",maxcollatz)

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))
