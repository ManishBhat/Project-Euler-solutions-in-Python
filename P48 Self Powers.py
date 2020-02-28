# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 23:02:33 2020

@author: manis
"""
def main():
    sum=0
    for i in range(1,1001):
        sum+=(i**i)
    print(sum%(10**10))
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 