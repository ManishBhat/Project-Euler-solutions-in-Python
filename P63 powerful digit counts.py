# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:43:41 2020

@author: manis_apezuzf
"""
from math import ceil
def main():
    n=1
    no_of_n_digit_positive_integers=0
    while ceil(10**(1-1/n))<10:
        no_of_n_digit_positive_integers+=10-ceil(10**(1-1/n))
        n+=1
    print(no_of_n_digit_positive_integers)

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time)) 