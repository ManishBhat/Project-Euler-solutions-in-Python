# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 11:33:07 2020

@author: manis_apezuzf
"""

import sympy
from sympy import isprime

def main():
    N=20000
    lst=list(sympy.sieve.primerange(1, N))
    sieveoferat=[0]*N
    lst.remove(2)
    lst.remove(5)
    print(lst)
    primeset_stack=[None]*N
    for i in range(len(lst)):
        for j in reversed(range(i)):
            x=int(str(lst[i])+str(lst[j]))
            if x<N:
                if lst[x]
            
            if isprime(int(str(lst[i])+str(lst[j])))==True:
                if isprime(int(str(lst[j])+str(lst[i])))==True:
                    primeset

    
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 