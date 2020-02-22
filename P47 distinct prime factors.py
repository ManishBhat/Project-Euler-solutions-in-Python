# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import math

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

def prime_list_generator(sieveoferat):
    lst=[]
    for i in range(len(sieveoferat)):
        if sieveoferat[i]==True:
          lst.append(i)
    return lst
def no_of_prime_factors(n,prime_num_list):
    i=0
    temp_n=n
    counter=0
    while prime_num_list[i]<=math.sqrt(n) and temp_n!=1:
       x=prime_num_list[i]
       if temp_n%x==0:
           counter+=1
           while temp_n%x==0:
               temp_n/=x
       i+=1    
    if temp_n!=1:
        counter+=1
    return counter
def main():
    N=10000
    sieveoferat=f(N)
    prime_num_list=prime_list_generator(sieveoferat)
    
    i=10
    counter=0
    val=4
    while counter<val:
        i+=1
        if no_of_prime_factors(i,prime_num_list)==val:
            counter+=1
        else:
            counter=0
    print(i-val+1)
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))     