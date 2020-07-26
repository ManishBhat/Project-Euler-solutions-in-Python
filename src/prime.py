# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 21:30:42 2020

@author: Manish
"""

def sieve_of_erat(N):
    """
    Function implements sieve of Eratosthenes (for all numbers uptil N).
    Returns array erat_sieve
    If erat_sieve[i] is True, then 2*i + 3 is a prime.
    """
    erat_sieve = [True]*int(N/2)
    prime_list = []
    prime_list.append(2)
    for i in range(int((math.sqrt(N)-3)/2)+1):  # Only need to run till sqrt(n)
        if erat_sieve[i] == True:
            j = i + (2*i+3)
            while j < int(N/2):
                erat_sieve[j] = False
                j += (2*i+3)
    for i in range(int(N/2)):
        if erat_sieve[i] == True:
            prime_list.append(2*i+3)
        
    return erat_sieve, prime_list

def is_prime(x, erat_sieve, prime_cache):
    """
    Parameters
    ----------
    x : int
        We are testing if x is prime
    erat_sieve : array of Bools
        This sieve tells us if number is prime or not
    prime_cache : dict with integer "key" and Bool "value"
        This cache is there so that we don't have to repeatedly do prime test.

    Returns
    -------
    TYPE: Bool
        If number is prime, returns True else False.

    """
    if x == 2:
        return True
    if x % 2 == 0:
        return False
    if x < len(erat_sieve):
        if erat_sieve[int((x-3)/2)] == True:
            return True
        else:
            return False
    else:
        prime_cache[x] = prime_cache.get(x, sympy.isprime(x))
        return prime_cache[x]

