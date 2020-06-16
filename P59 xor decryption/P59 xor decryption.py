# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:05:04 2020

@author: manis_apezuzf
"""

import enchant
d = enchant.Dict("en_US")
#print(d.check("Hello"))

#print('{0:07b}'.format(127))

def xor(num1,num2):
    return int(num1)^int(num2)
with open('p059_cipher.txt', 'r') as file:
    data = file.read().replace('\n','')
    data = data.replace('"', '')
    data=data.split(',')

for i in range(97,123):
    for j in range(97,123):
        for k in range(97,123):
            encr_key= ''.join(chr(i) for i in [i,j,k])
            if d.check(encr_key)==True:
                p=2
                while(p<len(data)):
                   wor=''.join([chr(xor(data[p-2],i)),chr(xor(data[p-1],j)),chr(xor(data[p],k))])
                   if d.check(wor)==False:
                       break
print(encr_key)                   
