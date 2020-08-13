# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 18:59:04 2020

@author: manis_apezuzf
"""

def Q700_v1(): # This is too slow (takes hours!)
    d = 1_504_170_715_041_707 
    modulo = 4503599627370517
    eulercoin = 1504170715041707
    x=d
    counter = 1
    print(counter, 1, eulercoin)
    for n in range(2,1_000_000_000):
        x=(d+x) % modulo
        if x<eulercoin:
            eulercoin = x
            counter+=1
            print(counter, n, eulercoin)

def Q700_v2(): #Generates all eulercoins in less than 1ms!
    d = 1_504_170_715_041_707 
    p = 4_503_599_627_370_517 # Modulus
    e = d # Euler coin (1st euler coin initialized to d)
    v = 0 
    coin_sum = e 
    for counter in range(1, 110):
    	print(counter, e) # Printing euler coins out of curiosity.
    	t = ((p-v)//e)*e
    	v += t
    	e = (v+e)%p # Generating next euler coin
    	coin_sum += e # Summing up euler coins
    	if e == 1:
    		print(counter + 1, e)
    		print("Total number of euler coins are:", counter + 1)
    		print("The sum is:", coin_sum) # Final answer
    		break

    

if __name__ == '__main__':
    import time
    start_time = time.time()
    Q700_v2()
    print("Program run time(in s): ", (time.time() - start_time)) 


