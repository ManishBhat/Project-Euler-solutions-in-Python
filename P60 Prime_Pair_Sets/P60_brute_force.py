# -*- coding: utf-8 -*-
"""
Created on Wed Jul 15 16:52:59 2020

@author: Manish
"""

from math import sqrt
from numba import jit
import time
import sympy

@jit
def sieve_of_erat(N):
    """
    Function implements sieve of Eratosthenes (for all numbers uptil N).
    Returns array erat_sieve
    If erat_sieve[i] is True, then 2*i + 3 is a prime.
    """
    erat_sieve = [True]*int(N/2)
    prime_list = []
    prime_list.append(2)
    for i in range(int((sqrt(N)-3)/2)+1):  # Only need to run till sqrt(n)
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


def is_primepair(a, b, erat_sieve, prime_cache, pair_cache):
    if (a,b) in pair_cache:
        return pair_cache[(a,b)]
    c1 = int(str(a)+str(b))
    c2 = int(str(b)+str(a))
    if is_prime(c1, erat_sieve, prime_cache):
        if is_prime(c2, erat_sieve, prime_cache):
            pair_cache[(a,b)] = True
            return True
    pair_cache[(a,b)] = False
    return False


def main():
    N = 10_000_000
    #N = 100
    erat_sieve, _ = sieve_of_erat(N)
    N = 20_000
    _, prime_list = sieve_of_erat(N)
    prime_list.remove(2)
    prime_list.remove(5)
    prime_cache = {}
    pair_cache = {}
    fargs = erat_sieve, prime_cache, pair_cache
    #print(prime_list)
    for i in range(len(prime_list)):
        a1 = prime_list[i]
        for j in range(i+1,len(prime_list)):
            a2 = prime_list[j]
            if is_primepair(a1, a2, erat_sieve, prime_cache, pair_cache):
                for k in range(j+1, len(prime_list)):
                    a3 = prime_list[k]
                    if is_primepair(a1, a3, erat_sieve, prime_cache, pair_cache) and is_primepair(a2, a3, erat_sieve, prime_cache, pair_cache):
                        for m in range(k+1, len(prime_list)):
                            a4 = prime_list[m]
                            if is_primepair(a1, a4, erat_sieve, prime_cache, pair_cache) and is_primepair(a2, a4, erat_sieve, prime_cache, pair_cache) and is_primepair(a3, a4, erat_sieve, prime_cache, pair_cache):
                                for p in range(m+1, len(prime_list)):
                                    a5 = prime_list[p]
                                    if is_primepair(a1, a5, erat_sieve, prime_cache, pair_cache) and is_primepair(a2, a5, erat_sieve, prime_cache, pair_cache) and is_primepair(a3, a5, erat_sieve, prime_cache, pair_cache) and is_primepair(a4, a5, erat_sieve, prime_cache, pair_cache):
                                        print(f"{a1} + {a2} + {a3} + {a4} + {a5} = {a1+a2+a3+a4+a5}")


if __name__ == "__main__":
    start_time = time.time()
    main()
    print("Time taken (in s): ", time.time() - start_time)


def test_is_prime():
    N = 10_000_000
    #N = 100
    a, prime_list = sieve_of_erat(N)
    x = 20_011
    print(f"{x} is prime: {is_prime(x, a)}")


'''
for i in range(int(N/2)):
    if a[i] == True:
        print(2*i+3)        
'''