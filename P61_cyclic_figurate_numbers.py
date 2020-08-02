#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 00:02:41 2020

@author: manish
"""

"""
This code is quite long even after accounting for the commenting.
The code uses 6 nested for loops. There is definetely a more elegant way
of solving this. However, thankfully it is extremely fast to run.
"""

class poly_num: # Creating class for polygonal numbers.

    def __init__(self, num, num_type):
        self.num = num
        self.type = num_type



def tri(f2d):
    """
    This function adds all 4-digit triangular numbers to f2d.

    Parameters
    ----------
    f2d : List containing 100 lists (consisting of poly_num objects)
        This list stores polygonal numbers based on the first 2 digits.
        For example, 8128 will be stored in f2d[81] 

    Returns
    -------
    None.

    """
    n = 0
    while True:
        n += 1
        num = int(n*(n+1)/2)
        if num >= 10_000:  # If the number is greater than 10_000 exit loop.
            break
        if num < 1000:  # Don't add numbers unless it is greater than 1000.
            continue
        pnum = poly_num(num, 'tri')  # Note 'tri' denotes triangular number.
        f2d[int(num/100)].append(pnum)  # Append 4-digit number(abcd) to f2d[ab] 


def sq(f2d):
    """
    This function adds all 4-digit square numbers to f2d.

    Parameters
    ----------
    f2d : List containing 100 lists (consisting of poly_num objects)
        This list stores polygonal numbers based on the first 2 digits.
        For example, 8128 will be stored in f2d[81] 

    Returns
    -------
    None.

    """
    n = 0
    while True:
        n += 1
        num = n**2
        if num >= 10_000:  # If the number is greater than 10_000 exit loop.
            break
        if num < 1000:  # Don't add numbers unless it is greater than 1000.
            continue
        pnum = poly_num(num, 'sq')  # Note 'sq' denotes square number.
        f2d[int(num/100)].append(pnum)  # Append 4-digit number(abcd) to f2d[ab]


def pent(f2d):
    """
    This function adds all 4-digit pentagonal numbers to f2d.

    Parameters
    ----------
    f2d : List containing 100 lists (consisting of poly_num objects)
        This list stores polygonal numbers based on the first 2 digits.
        For example, 8128 will be stored in f2d[81] 

    Returns
    -------
    None.

    """
    n = 0
    while True:
        n += 1
        num = int(n*(3*n-1)/2)
        if num >= 10_000:  # If the number is greater than 10_000 exit loop.
            break
        if num < 1000:  # Don't add numbers unless it is greater than 1000.
            continue
        pnum = poly_num(num, 'pent')  # Note 'pent' denotes pentagonal number.
        f2d[int(num/100)].append(pnum)  # Append 4-digit number(abcd) to f2d[ab]


def hexag(f2d):
    """
    This function adds all 4-digit hexagonal numbers to f2d.

    Parameters
    ----------
    f2d : List containing 100 lists (consisting of poly_num objects)
        This list stores polygonal numbers based on the first 2 digits.
        For example, 8128 will be stored in f2d[81] 

    Returns
    -------
    None.

    """
    n = 0
    while True:
        n += 1
        num = n*(2*n-1)
        if num >= 10_000:  # If the number is greater than 10_000 exit loop.
            break
        if num < 1000:  # Don't add numbers unless it is greater than 1000.
            continue
        pnum = poly_num(num, 'hex')  # Note 'hex' denotes hexagonal number.
        f2d[int(num/100)].append(pnum)  # Append 4-digit number(abcd) to f2d[ab]


def hepta(f2d):
    """
    This function adds all 4-digit heptagonal numbers to f2d.

    Parameters
    ----------
    f2d : List containing 100 lists (consisting of poly_num objects)
        This list stores polygonal numbers based on the first 2 digits.
        For example, 8128 will be stored in f2d[81] 

    Returns
    -------
    None.

    """
    n = 0
    while True:
        n += 1
        num = int(n*(5*n-3)/2)
        if num >= 10_000:  # If the number is greater than 10_000 exit loop.
            break
        if num < 1000:  # Don't add numbers unless it is greater than 1000.
            continue
        pnum = poly_num(num, 'hept')  # Note 'hept' denotes heptagonal number.
        f2d[int(num/100)].append(pnum)  # Append 4-digit number(abcd) to f2d[ab]


def octa(f2d):
    """
    This function adds all 4-digit octagonal numbers to f2d.

    Parameters
    ----------
    f2d : List containing 100 lists (consisting of poly_num objects)
        This list stores polygonal numbers based on the first 2 digits.
        For example, 8128 will be stored in f2d[81] 

    Returns
    -------
    None.

    """
    n = 0
    while True:
        n += 1
        num = n*(3*n-2)
        if num >= 10_000:  # If the number is greater than 10_000 exit loop.
            break
        if num < 1000:  # Don't add numbers unless it is greater than 1000.
            continue
        pnum = poly_num(num, 'oct')  # Note 'oct' denotes octagonal number.
        f2d[int(num/100)].append(pnum)  # Append 4-digit number(abcd) to f2d[ab]


def main():
    '''
    Main code to generate 6 cyclical polygonal numbers.

    Returns
    -------
    None.

    '''
    
    # f2d : List containing 100 lists (consisting of poly_num objects)
    # This list stores polygonal numbers based on the first 2 digits.
    # For example, 8128 will be stored in f2d[81] 
    f2d = [ [] for _ in range(100) ] # Creating a list containing 100 empty lists.
    tri(f2d)  # Adds triangular numbers to f2d
    sq(f2d)  # Adds square numbers to f2d
    pent(f2d)  # Adds pentagonal numbers to f2d
    hexag(f2d)  # Adds hexagonal numbers to f2d
    hepta(f2d)  # Adds heptagonal numbers to f2d
    octa(f2d)  # Adds octagonal numbers to f2d


# This is a quite ugly set of 6 nested loops. I am testing for the cyclical nature of the 6 polygonal numbers.
    for ind in range(100):  # Running over the entire f2d array (Remember that it contains 100 lists.)
        ntype = [] # ntype is an array that will store the type of the polygonal number.
                   # ntype ensures that the 6 polygonal numbers have distinct types (as required by Problem 61.)
        if f2d[ind] is None:  #If f2d[ind] is empty, it would generate an error in the for loop below. These 2 lines prevent that.
            continue
        for x1 in f2d[ind]: # For loop iterating over x1.
            ntype.append(x1.type) # Appending the type of x1 to ntype.
            if f2d[x1.num%100] is None: # Prevents error in for loop below.
                ntype.pop()  # Removing x1.type from ntype as we will be returning to the loop beginning.
                continue
            for x2 in f2d[x1.num%100]: # IMP!!!! Accesing only the numbers with first 2 digits same as last 2 digits of x1. Ensure cyclical nature of x1 & x2.
                if x2.type not in ntype: # Ensure that x1 and x2 are different types of polygonal numbers.
                    ntype.append(x2.type) # Add x2.type to ntype.
                    if f2d[x2.num%100] is None:
                        ntype.pop()
                        continue
                    for x3 in f2d[x2.num%100]: # IMP!!!! Accesing only the numbers with first 2 digits same as last 2 digits of x2. Ensure cyclical nature of x2 & x3.
                        # And so on... Remainder of the loops are to add x4, x5 and x6.
                        if x3.type not in ntype:
                            ntype.append(x3.type)
                            if f2d[x3.num%100] is None:
                                ntype.pop()
                                continue
                            for x4 in f2d[x3.num%100]:
                                if x4.type not in ntype:
                                    ntype.append(x4.type)
                                    if f2d[x4.num%100] is None:
                                        ntype.pop()
                                        continue
                                    for x5 in f2d[x4.num%100]:
                                        if x5.type not in ntype:
                                            ntype.append(x5.type)
                                            if f2d[x5.num%100] is None:
                                                ntype.pop()
                                                continue
                                            for x6 in f2d[x5.num%100]:
                                                if x6.type not in ntype:
                                                    ntype.append(x6.type)
                                                    if f2d[x6.num%100] is None:
                                                        ntype.pop()
                                                        continue
                                                    if x1 in f2d[x6.num%100] :
                                                        # Woo hoo!!! Reaching here means that x1, x2, x3, x4, x5 and x6 are distinct and cyclic.
                                                        print(x1.num, x2.num, x3.num, x4.num, x5.num, x6.num)
                                                        print(x1.type, x2.type, x3.type, x4.type, x5.type, x6.type)
                                                        print(f"Sum is : {x1.num + x2.num + x3.num + x4.num + x5.num + x6.num}") # The answer!! :) 
                                                        return
                                                    ntype.pop()  # Cleaning out x6
                                            ntype.pop()  # Cleaning out x5
                                    ntype.pop()  # Cleaning out x4
                            ntype.pop()  # Cleaning out x3
                    ntype.pop()  # Cleaning out x2
            ntype.pop()  # Cleaning out x1                                      
if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))
                            
                    
        