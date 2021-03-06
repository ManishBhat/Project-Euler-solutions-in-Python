# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 16:25:10 2020

@author: manis_apezuzf
"""
from math import sqrt
def f(n):   #This code will find the sum of all primes below n
    sieveoferat=[True]*n
    sieveoferat[0]=sieveoferat[1]=False
    listofprimes=[]
    for i in range(2,n):
        if(sieveoferat[i]==True):
            listofprimes.append(i)
            j=2
            while(j*i<n):
                sieveoferat[j*i]=False
                j=j+1
    return sieveoferat
def isPrime(n):
    if n<2:
        return False
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            return False
    return True
def main():
    counter=0
    n=2
    while True:
        diagelements=[4*n*n-10*n+7,4*n*n-8*n+5,4*n*n-6*n+3,(2*n-1)**2]
        for x in diagelements:
            if isPrime(x):
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