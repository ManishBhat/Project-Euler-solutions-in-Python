# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 02:31:10 2019

@author: manis
"""
'''
with open("P11.txt") as f:
    contents=[]
    [contents.append(x) for x in f]
    print(contents)
    contents = [ x for x in contents if x.isdigit() ] #This line is for removing all non-numeric characters from string
    print(contents)
'''
'''
f= open("P11.txt","r")
contents=[]
for x in f:
    contents.append(x.strip('\n'))
print(len(contents))
for i in range(len(contents)):
    print(contents[i])
print(contents[25])
'''
# This opens a handle to your file, in 'r' read mode
f = open('P11.txt', 'r')
# Read in all the lines of your file into a list of lines
lines_list = f.readlines()
# Does a double-nested list comprehension to get into the matrix
a=[[int(val) for val in line.split()] for line in lines_list[0:]]

maxprod=1
#Read horizontally
for i in range(20):
    for j in range(17):
        prod=a[i][j]*a[i][j+1]*a[i][j+2]*a[i][j+3]
        if prod>maxprod:
            maxprod=prod
print(maxprod)
maxprod=1
#Read vertically
for i in range(17):
    for j in range(20):
        prod=a[i][j]*a[i+1][j]*a[i+2][j]*a[i+3][j]
        if prod>maxprod:
            maxprod=prod
print(maxprod)
maxprod=1
#Read diagonally
for i in range(17):
    for j in range(17):
        prod=a[i][j]*a[i+1][j+1]*a[i+2][j+2]*a[i+3][j+3]
        if prod>maxprod:
            maxprod=prod
print(maxprod)
maxprod=1
#Read in reverse diagonal
for i in range(3,20):
    for j in range(17):
        prod=a[i][j]*a[i-1][j+1]*a[i-2][j+2]*a[i-3][j+3]
        if prod>maxprod:
            maxprod=prod
print(maxprod)        
        
    
        
