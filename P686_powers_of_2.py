# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 19:26:32 2020

@author: Manish
"""
import sys, time
from math import log10
from numba import jit

@jit
def Q686():
    N = 100_000_000
    L = 123
    logL = log10(L)
    logL1 = log10(L+1)
    log2 = log10(2)
    counter = 1
    for x in range(N):
        n1 = int((x+logL)/log2)
        n2 = int((x+logL1)/log2)
        if n1 != n2:
            counter += 1
            if counter == 678910:
                print(n2)
if __name__ == "__main__":
    start_time = time.time()
    Q686()
    print("Program run time(in s): ", (time.time() - start_time))