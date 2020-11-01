# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 19:07:40 2020

@author: Manish
"""
from math import sqrt


def Q88():
    range_of_k = 12000
    N = 2*range_of_k
    # Array a stores a set of tuples for each number
    # 1st tuple element is sum of factors and the 2nd is number of factors
    a = [set() for i in range(N+1)]
    for i in range(2, N+1):
        a[i].add((i, 1))
    for i in range(2, N+1):
        for x in range(2, int(sqrt(i))+1):
            if i % x == 0:
                for sof, nof in a[i//x]:
                    a[i].add((sof+x, nof+1))
    
    d = {}
    set_of_product_sum_nos = set()
    for n in range(2, N+1):
        for sof, nof in a[n]:
            k = n - sof + nof
            if 2 <= k <= range_of_k:
                if k not in d:
                    d[k] = n
                    set_of_product_sum_nos.add(n)
    print(sum(set_of_product_sum_nos))


if __name__ == '__main__':
    import time
    start_time = time.time()
    Q88()
    print("Program run time(in s): ", (time.time() - start_time))

