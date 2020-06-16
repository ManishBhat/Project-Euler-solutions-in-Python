# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:25:10 2020

@author: manis_apezuzf
"""
from sympy import isprime

def main():
    counter=0
    n=2
    while True:
        diagelements=[4*n*n-10*n+7,4*n*n-8*n+5,4*n*n-6*n+3,(2*n-1)**2]
        for x in diagelements:
            if isprime(x):
                counter+=1
                #print(x)
        #print(counter,4*n-3)
        if (counter/(4*n-3))<0.1:
            break
        n+=1
    print("The side length is: ",2*n-1)

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 