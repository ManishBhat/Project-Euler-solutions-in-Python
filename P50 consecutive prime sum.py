# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 00:24:14 2020

@author: manis
"""

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

def main():
    N=10**6
    sieveoferat=f(N)
    prime_num_list=prime_list_generator(sieveoferat)
    arr=[0]*(len(prime_num_list)+1)
    arr[0]=0
    for i in range(1,len(arr)):
        arr[i]=arr[i-1]+prime_num_list[i-1]
    
    maxdiff=0
    logest_prime_sum=41
    start_prime=2
    stop_prime=13
    for i in range(len(arr)):
        for j in range(i+maxdiff+1,len(arr)):
            if arr[j]-arr[i]>=N:
                break
            if sieveoferat[arr[j]-arr[i]]==True:
                maxdiff=j-i
                start_prime=prime_num_list[i]
                stop_prime=prime_num_list[j-1]
                longest_prime_sum=arr[j]-arr[i]
                
    print("The first prime in the sequence is: ",start_prime)
    print("The last prime in the sequence is: ",stop_prime)
    print("The number of terms in the sequence is: ",maxdiff)
    print("The prime below one million that can be written as the sum \
of the most consecutive primes is: ",longest_prime_sum)

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))    