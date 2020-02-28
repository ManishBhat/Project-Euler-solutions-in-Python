# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 02:34:05 2020

@author: manis
"""
def main():
    import math
    fact=[0]*101
    for n in range(101):
        fact[n]=math.factorial(n)
    counter=0
    for n in range(1,101):
        for r in range(n+1):
            if (fact[n]/(fact[n-r]*fact[r]))>10**6:
                counter+=1
    print(counter)
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))