# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 03:25:32 2019

@author: manis
"""
import math
import sys

def number_of_divisors(N):
    N=int(N)
    n=N
    numofdiv=1
    for i in range(2,int(math.sqrt(N)+1)):
        k=1
        while(n%i==0):
            k=k+1
            n=n/i
        numofdiv=numofdiv*k
    if(n!=1):  #If there is a prime factor greater than sqrt(N) eg. 11 is larger than sqrt(33)
        numofdiv=numofdiv*2
    return numofdiv

def main(L):
    print(number_of_divisors(28))
    n=1
    while 1: 
        if n%2==0:
            numofdiv=number_of_divisors(n/2)*number_of_divisors(n+1)
        else:
            numofdiv=number_of_divisors(n)*number_of_divisors((n+1)/2)
        if numofdiv>L:
            print(n*(n+1)/2,numofdiv)
            return 1
        n=n+1
if __name__ == "__main__":
    main(500)