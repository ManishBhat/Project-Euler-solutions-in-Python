# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 01:47:26 2020

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

def Q124():
    N = 1_00_000
    _, plist = sieve_of_erat(sqrt(N))
    
    def rad(n, plist):
        ans = 1
        for p in plist:
            if n%p == 0:
                ans *= p
                while n%p ==0:
                    n//=p
        ans *= n
        return ans
    
    E = [(0,0)]
    for i in range(1,N+1):
        pass
        E.append((i,rad(i, plist)))
    E.sort(key = lambda kv: kv[1])
    print(E[10_000][0])

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q124()
    print("Program run time(in s): ", (time.time() - start_time))