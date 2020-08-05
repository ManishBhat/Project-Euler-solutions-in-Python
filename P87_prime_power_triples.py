# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 10:59:26 2020

@author: Manish
"""
from math import sqrt

def sieve_of_erat(N):
    """
    Function implements sieve of Eratosthenes (for all numbers uptil N).
    Returns array erat_sieve
    If erat_sieve[i] is True, then 2*i + 3 is a prime.
    """
    lim = int(N/2)
    if N % 2 == 0:
        lim -= 1
    erat_sieve = [True]*lim
    prime_list = []
    prime_list.append(2)
    for i in range(int((sqrt(N)-3)/2)+1):  # Only need to run till sqrt(n)
        if erat_sieve[i] == True:
            j = i + (2*i+3)
            while j < lim:
                erat_sieve[j] = False
                j += (2*i+3)
    for i in range(lim):
        if erat_sieve[i] == True:
            prime_list.append(2*i+3)
        
    return erat_sieve, prime_list

def Q87():
    N = 50_000_000
    _, prime_list = sieve_of_erat(int(sqrt(N)))
    d = {}
    sq = []
    cube = []
    quad = []
    for p in prime_list:
        sq.append(p**2)
        cube.append(p**3)
        quad.append(p**4)
    for n1 in sq:
        for n2 in cube:
            if n1 + n2 >= N: break
            for n3 in quad:
                val = n1 + n2 + n3
                if val >=N: break
                d[val] = True
    print(len(d))

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q87()
    print("Program run time(in s): ", (time.time() - start_time)) 