# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:01:37 2020

@author: manis
"""
from gmpy2 import is_square
from math import sqrt
def return_n_of_hnANDtn(a):
    if is_square(1+8*a):
        x=int(sqrt(1+8*a))
        if x%2==1 and x%4==3:
            return True
    return False
    
def main():
    n=166
    while True:
        pn=int(n*(3*n-1)/2)
        if return_n_of_hnANDtn(pn)==True:
            print(pn)                
            return
        n+=1
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 