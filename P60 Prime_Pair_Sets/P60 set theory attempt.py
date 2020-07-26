# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:33:07 2020

@author: manis_apezuzf
"""

import sympy
from sympy import isprime

def main():
    N=100
    prime_sieve=list(sympy.sieve.primerange(1, N))
    prime_sieve.remove(2)
    prime_sieve.remove(5)
    prime_tuples = set()
    max_set_len = 0
    max_set = set()

    for num1 in prime_sieve:
        notprime = set()  # Numbers with which concanetanting num1 doesn't give a prime
        for num2 in prime_sieve:
            if num2 >= num1:
                break
            concat1 = int(str(num1) + str(num2))
            concat2 = int(str(num2) + str(num1))
            if not(isprime(concat1)) or not(isprime(concat2)):
                notprime.add(num2)
        new_set = set()
        
        for prime_tuple in prime_tuples:
            temp_set = set(prime_tuple)
            if notprime.isdisjoint(temp_set):
                temp_set.add(num1)
                new_set.update(temp_set)
                if max_set_len < len(temp_set):
                    max_set_len = len(temp_set)
                    max_set = temp_set
        if len(new_set) !=0:
            prime_tuples.add(tuple(new_set))
        prime_tuples.add((num1,))
    print("The max set is:", max_set)
    

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 