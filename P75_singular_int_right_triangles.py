# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 08:55:32 2020

@author: Manish
"""
from math import gcd, sqrt

def Q75():
    T = 1_500_000
    arr = [0]* T
    for m in range(1,int(sqrt(T/2))+1):
        for n in range(1, m):
            if 2*m*(m+n) > T:
                break
            if gcd(m,n) == 1 and m%2 != n%2:
                k = 1
                while True:
                    triplet_sum = 2*k*m*(m+n)
                    if triplet_sum >= T:
                        break
                    arr[triplet_sum] += 1
                    k += 1
        m += 1

    counter = 0
    for i in range(T):
        if arr[i] == 1:
            counter += 1
    print(counter)
    
if __name__ == "__main__":
    import time
    start_time = time.time()
    Q75()
    print("Time taken (in s): ", time.time() - start_time)
