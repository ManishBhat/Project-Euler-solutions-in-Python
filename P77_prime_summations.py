# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 14:14:52 2020

@author: Manish
"""
from math import sqrt
from numba import jit

@jit
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

def Q77():
    N = 101
    _, prime_list = sieve_of_erat(N)
    arr = [[0]*len(prime_list) for i in range(N+1)]

    for i in range(len(prime_list)):
        arr[0][i] = arr[2][i] = 1
    for n in range(2,N+1):
        if n%2 == 0:
            arr[n][0] = 1
        else:
            arr[n][0] = 0

    for n in range(3, N+1):
        for i in range(1,len(prime_list)):
            if n - prime_list[i] >=0:
                arr[n][i] = arr[n][i-1] + arr[n-prime_list[i]][i]
            else:
                arr[n][i] = arr[n][i-1]

    for n in range(3, N+1):
        if arr[n][len(prime_list) - 1] > 5000:
            print(n)  # Our answer!
            break


if __name__ == '__main__':
    import time
    start_time = time.time()
    #Q77()
    sieve_of_erat(100_000_000)
    print("Program run time(in s): ", (time.time() - start_time)) 