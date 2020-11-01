# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 15:48:06 2020

@author: Manish
"""
from math import gcd
from numba import jit



@jit
def Q73():
    N = 12000
    ans = 0
    for d in range(1, N+1):
        t1 = d//3 + 1
        t2 = (d-1)//2
        for n in range(t1, t2 + 1):
            #print(n,"/",d)
            if gcd(d, n) == 1:
                    ans += 1
    print(ans)

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q73()
    print("Program run time(in s): ", (time.time() - start_time)) 