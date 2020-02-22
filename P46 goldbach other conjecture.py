# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 16:24:54 2020

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

def main():
    N=10000
    sieveoferat=f(N)
    n=33
    while True:
        if sieveoferat[n]==False:
            k=1
            opt=True
            while n-2*k*k >= 3:
                if sieveoferat[n-2*k*k]==True:
                    opt=False
                    break
                k+=1
            if opt==True:
                print(n)
                return
        n+=2
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 