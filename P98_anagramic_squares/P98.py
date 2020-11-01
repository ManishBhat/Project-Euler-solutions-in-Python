# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 21:31:28 2020

@author: Manish
"""
from math import sqrt, ceil
from itertools import combinations

def read_file(fname):
    fhand = open(fname,"r")
    for line in fhand:
        x = line.strip().split(',')
        arr = [mystr.replace('"', '') for mystr in x]
        return arr


def find_anagrams(arr):
    """
    Take in raw array with the words, and identify anagramic words.

    Returns dictionary of anagramic pairs or tripet.
    """
    d = {}
    for mystr in arr:
        sort_mystr = ''.join(sorted(mystr))
        d[sort_mystr] = d.get(sort_mystr, [])
        d[sort_mystr].append(mystr)
    d = {k:v for k,v in d.items() if len(v) != 1}
    return d

def anagram_mapping(word1, word2):
    d = {}
    for i in range(len(word2)):
        d[word2[i]] = d.get(word2[i], [])
        d[word2[i]].append(i)
    lst, i = [], 0
    for x in word1:
        lst.append(d[x][0])
        del d[x][0]
    return lst



def find_anagramic_number(anag_map, n1, word1, word2):
    
    n1 = str(n1)
    n2 = [-1]*len(n1)
    for i in range(len(anag_map)):
        n2[anag_map[i]] = n1[i]

    n2 = int(''.join(map(str,n2)))
    return n2

def check_valid(num, word):
    num = str(num)
    d ={}
    for i, let in zip(num, word):
        if i in d and d[i]!=let:
            return False
        else:
            d[i] = let
    return True
        

def find_anagramic_square(word1, word2):
    L = len(word1)
    n = ceil(sqrt(10**(L-1)))
    lst = anagram_mapping(word1, word2)
    max_n2 = 0
    while n**2 <10**L:
        if check_valid(n**2, word1) is False:
            n+=1
            continue
        n2_squared = find_anagramic_number(lst, n**2, word1, word2)
        if n2_squared < 10**(L-1) or check_valid(n2_squared, word2) is False:
            n+=1
            continue
        n2 = sqrt(n2_squared)
        if n2 == int(n2):
            n2 = int(n2)
            if max_n2 < n2:
                max_n2 = n2
        n+=1
    return max_n2

def find_max_anagram_row(word_list):
    r = combinations(word_list,2)
    max_n = 0
    for word1, word2 in r:
        max_n = find_anagramic_square(word1, word2)
    return max_n


def q98():
    arr = read_file("p098_words.txt")
    d = find_anagrams(arr)
    max_n = 0
    for k,v in d.items():
        n = find_max_anagram_row(v)
        if max_n < n:
            max_n = n
    print(max_n**2)


if __name__ == "__main__":
    import time
    start_time  = time.time()
    q98()
    print("Time elapsed is in (s):", time.time()-start_time)