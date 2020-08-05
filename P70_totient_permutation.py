# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 13:17:43 2020

@author: Manish
"""


def Q70():
    N = 10_000_000
    totient = [i for i in range(N+1)]
    for i in range(2, N+1):
        if totient[i] == i:
            for j in range(i, N+1, i):
                totient[j] -= totient[j] // i
    min_i = 0
    min_val = 1000
    for i in range(2, N+1):
        if sorted(str(i)) == sorted(str(totient[i])):
            if min_val > i/totient[i]:
                min_val = i/totient[i]
                min_i = i
    print(min_i)

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q70()
    print("Program run time(in s): ", (time.time() - start_time)) 