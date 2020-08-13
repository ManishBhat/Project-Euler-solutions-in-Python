# -*- coding: utf-8 -*-
"""
Created on Wed Aug 12 17:56:03 2020

@author: Manish
"""
import time


def S(n, modulo): 
    #Note doing power without modulo is impossible as n//9 becomes as large as 10^90
    #sometimes. In other words we have to deal with numbers as big as 10^(10^90).
    #The above number has 10^90 digits, more than the atoms in the universe.
    # But, thanks to modulo and pow (thanks Python!) this is a 1 line solution.
    v =pow(10, n//9, modulo) # Holy crap, this is awesome!
    #The formula was derived for S(n).
    return (6*(v-1) - 9*(n//9) + v*(2*(n%9)+((n%9)*(n%9-1))//2) - n%9)%modulo


def Q684():
    f1 = 0
    f2 = 1
    N=90
    modulo = 1_000_000_007
    suma = 0
    arr = []
    
    #Generating fibonacci series
    for i in range(N+1):
        arr.append(f1)
        temp = f2
        f2 = f1+f2
        f1 = temp
    
    #Summing up the values
    for x in arr[2:]:
        suma = (suma + S(x, modulo))%modulo
    print(suma)

if __name__ == "__main__":
    start_time = time.time()
    Q684()
    print("Program run time(in s): ", (time.time() - start_time))