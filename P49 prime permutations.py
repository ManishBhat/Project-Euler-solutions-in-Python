# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:17:50 2020

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
    for a1 in range(1488,N):
        d=1
        while a1+2*d<N:
            if sieveoferat[a1]==sieveoferat[a1+d]==sieveoferat[a1+2*d]==True:
                if ''.join(sorted(str(a1)))==''.join(sorted(str(a1+d))):
                    if ''.join(sorted(str(a1)))==''.join(sorted(str(a1+2*d))):
                        print(str(a1)+str(a1+d)+str(a1+2*d))
                        return
            d+=1
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))       