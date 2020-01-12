# -*- coding: utf-8 -*-
"""
Created on Sun Jan 12 00:42:21 2020

@author: manis
"""
import csv
  
def stringtoNum(input_string):
    tempstr=input_string
    sum=0
    for i in range(len(tempstr)):
        sum = sum + ord(tempstr[i]) - 64
    return sum
   
with open(r'p022_names.txt') as f:
    input_data = []
    for row in csv.reader(f, delimiter=',', quoting=csv.QUOTE_NONE):
        input_data += row

for i in range(len(input_data)):
    input_data[i]= input_data[i].replace('"', '')
input_data.sort() 

sum=0
for i in range(len(input_data)):
    sum = sum + (i+1)*stringtoNum(input_data[i])
print(sum)

