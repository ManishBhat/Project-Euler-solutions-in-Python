# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:59:04 2020

@author: manis_apezuzf
"""
import math
def main():
    from sympy import isprime, primefactors
    d=1504170715041707
    T=4503599627370517
    eulercoin=1504170715041707
    sum=eulercoin
    '''
    x=1504170715041707
    for n in range(2,100000000):
        x=(1504170715041707+x)%4503599627370517
        if x<eulercoin:
            eulercoin=x
            counter+=1
    print(eulercoin,counter)
    '''
    delta=3-T/d
    n=2
    while True: 
        k=int(n*d/T)
        while True:
            if math.ceil(k*T/d)==int((eulercoin+k*T)/d):
                n=int((eulercoin+k*T)/d)
                eulercoin=(n*d)%T
                print(eulercoin,k,n)
            else:
                k+=int(1/delta)+1
                
    
    
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 


