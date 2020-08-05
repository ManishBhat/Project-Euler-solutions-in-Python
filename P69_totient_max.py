# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 12:28:21 2020

@author: Manish
"""
from math import sqrt
from numba import jit
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


def totient(a, prime_list):
    n = a
    ans = n
    if n in prime_list:
        return (n-1)
    for p in prime_list:
        if n%p == 0:
            ans = (ans//p) *(p-1)
            while n%p ==0:
                n//=p
        if n==1:
            return ans
    return  (ans//n)*(n-1)

def Q69_v1():
    N = 1_000_000
    _, prime_list = sieve_of_erat(sqrt(N))
    '''
    for i in range(2, N+1):
        print(i, totient(i, prime_list))
    '''
    max_n = 0
    max_val = 0
    for i in range(2, N+1):
        val = i/totient(i, prime_list)
        if max_val < val:
            max_val = val
            max_n = i
    print(max_n, max_val)
    print(2*3*5*7*11*13*17)

@jit
def Q69_v2():
    N = 1_000_000
    max_val = 0
    max_i = 0
    totient = [i for i in range(N+1)]
    for i in range(2, N+1):
        if totient[i] == i:
            for j in range(i, N+1, i):
                totient[j] -= totient[j] // i
        val = i/totient[i]
        if max_val < val:
            max_val = val
            max_i = i
    print(max_i)

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q69_v2() # Version 2 is much faster than version 1.
    print("Program run time(in s): ", (time.time() - start_time)) 