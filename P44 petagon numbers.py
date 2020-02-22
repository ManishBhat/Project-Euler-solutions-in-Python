# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 15:03:35 2020

@author: manis
"""

import gmpy2
import sys
from math import sqrt
def Pn(n):
    return int(n*(3*n-1)/2)
def return_n_of_pn(pn):
    if gmpy2.is_square(1+24*pn):
        if int(sqrt(1+24*pn))%6==5:
            return int((1+int(sqrt(1+24*pn)))/6)
    return -1
def main():
    import time
    start_time = time.time()
    N=10000
    for i in range(1,N):
        for j in range(i+1,N):
            d=Pn(i)
            s=Pn(j)
            if (s-d)%2==0:
                a=return_n_of_pn(int((s-d)/2))
                b=return_n_of_pn(int((s+d)/2))
                if a>-1 and b>-1:
                    print(d)
                    print("Program run time(in s): ", (time.time() - start_time))
                    return
if __name__ == '__main__':
    main()
                
                