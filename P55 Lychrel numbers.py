# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 02:47:25 2020

@author: manis
"""

def is_palin(n): #Function to check if an integer n is a palindrome
    if str(n)==str(n)[::-1]:
        return True
    return False
def lychrel_counter(n,lychrel_counter_arr):
    counter=0
    sum=n
    if lychrel_counter_arr[n]>0:
        return lychrel_counter_arr[n]
    while counter<50:
        counter+=1
        sum=sum+int(str(sum)[::-1])
        if is_palin(sum):
            lychrel_counter_arr[n]=lychrel_counter_arr[int(str(n)[::-1])]=counter
            return counter
    return -1    

def main ():           
    N=10000       
    lychrel_counter_arr=[0]*N
    counter=0
    for i in range(195,N):
        if lychrel_counter(i,lychrel_counter_arr)==-1:
            counter+=1
    print(counter)

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))    