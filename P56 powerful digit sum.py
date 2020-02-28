# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 03:19:31 2020

@author: manis
"""
def main():
    maxdigitalsum=0
    maxa=0
    maxb=0
    for a in range(1,100):
        for b in range(1,100):
            sum=0
            x=str(a**b)
            for digits in x:
                sum+=int(digits)
            if maxdigitalsum<sum:
                maxdigitalsum=sum
                maxa=a
                maxb=b
    print("The number with the maximum digit sum is", maxa,"**",maxb)
    print("The sum of its digits is: ",maxdigitalsum)
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))   