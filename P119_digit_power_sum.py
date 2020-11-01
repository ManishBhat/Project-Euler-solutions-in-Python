# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 02:13:13 2020

@author: Manish
"""
from math import log
from numba import jit

def digitsum(n):
    return sum([int(d) for d in str(n)])

def Q102():
    nod = 20 # Number of digits we desire at most
    n = 10**nod
    n2 = int(log(n,2))
    arr = []

    for k in range(2,n2+1):
        a = 2
        while a<9*nod and a**k <n:
            val = a**k
            if a == digitsum(val):
                arr.append(val)
            a += 1
    
    arr.sort()
    print(arr[29])

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q102()
    print("Program run time(in s): ", (time.time() - start_time)) 