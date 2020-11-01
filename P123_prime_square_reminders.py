# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 00:43:13 2020

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


def Q123():
    N = 1_000_000
    N2 = 10**10
    
    _, plist = sieve_of_erat(N)
    for i in range(len(plist)):
        n = i+1
        p = plist[i]
        modulo = p**2
        r = (pow(p-1,n,modulo) + pow(p+1,n, modulo))% modulo
        if r > N2:
            print(n)
            break

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q123()
    print("Program run time(in s): ", (time.time() - start_time)) 