# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:42:39 2020

@author: manis_apezuzf
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
def d(N,prime_list): #This function returns the sum of the proper divisors.
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
sieveoferat=f(1000)
prime_list=prime_list_generator(sieveoferat)
N=100000
arr=[0]*N
arr[0]=arr[1]=-1
for n in range(2,N):
    x=d(n,prime_list)
    #print(x,n)
    if x==1 or x>=N or x==n or arr[x]==-1:
        arr[n]=-1
    else:
        p2=n
        while(True):
            #print(n,"Reached")
            arr[n]+=1
            p2=d(p2,prime_list)
            if p2==1 or p2>=N or arr[p2]==-1 or arr[n]>50:
                arr[n]=-1
                break
            elif p2==n:
                break
maxlen=0
max_n=2
for n in range(2,N):
    if arr[n]>maxlen:
       max_n=n
       maxlen=arr[n]
print(maxlen,max_n)

    