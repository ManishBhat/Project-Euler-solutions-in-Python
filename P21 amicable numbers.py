# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 16:11:48 2019

@author: manis
"""
#I am doing the amicable number problem

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
def d(N,prime_list):
    n=N
    sum=1
    for x in prime_list:
        ax=0
        while n%x==0:
            n=int(n/x)
            ax+=1
        sum*=int((x**(ax+1)-1)/(x-1))
    if n!=1:
        sum*=(n+1)
    sum=sum-N
    return sum


#print(d(220),d(284))
def main():
    sieveoferat=f(100)
    prime_list=prime_list_generator(sieveoferat)
    print(d(6,prime_list))
    arr=[0]*100000
    for n in range(1,10000):
       arr[n]=d(n,prime_list)
    for n in range(1,10000):
        if (arr[n]!=0 and arr[n]<10000 and arr[n]!=n):
            if arr[arr[n]]==n:
                print(n,arr[n])
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))    
        
        
    
