# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:24:57 2019

@author: manis
"""

def ispalin(N):
    x = str(N)
    if x == x[::-1]:
        return True
    return False

def Q4():
    largestpalin=1
    for i in range(100,1000):
        for j in range(100,1000):
            if(i*j>largestpalin):
                if ispalin(i*j):
                    largestpalin=i*j
    print(largestpalin)

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q4()
    print("Program run time(in s): ", (time.time() - start_time))