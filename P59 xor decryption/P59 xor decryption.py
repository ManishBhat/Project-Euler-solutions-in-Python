# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 12:05:04 2020

@author: manis_apezuzf
"""

import matplotlib.pyplot as plt
#import enchant
#d = enchant.Dict("en_US")
#print(d.check("Hello"))

#print('{0:07b}'.format(127))


def plot_dict(freq_counter):
    list_of_items = []
    for (k,v) in freq_counter.items():
        list_of_items.append((v,k))
    list_of_items.sort(reverse=True)
    
    myvalues, mykeys= zip(*list_of_items[:7])
    plt.bar(mykeys, myvalues, color='g')
    plt.title('Histogram of the 7 most common words')
    plt.show()
def Q59():    
    with open('p059_cipher.txt', 'r') as file:
        data = file.read().replace('\n','')
        data = data.replace('"', '')
        data=data.split(',')
    
    freq1 = dict()
    freq2 = dict()
    freq3 = dict()
    
    ind = 0
    while True:
        if ind < len(data):
            freq1[data[ind]] = freq1.get(data[ind], 0) + 1
            if ind + 1 < len(data):
                freq2[data[ind + 1]] = freq2.get(data[ind + 1], 0) + 1
                if ind + 2 < len(data):
                    freq3[data[ind + 2]] = freq3.get(data[ind + 2], 0) + 1
        else:
            break
        ind += 3

    plot_dict(freq1)
    plot_dict(freq2)
    plot_dict(freq3)
    
    # From this plot I got to know that 80 is the most frequently appearing number.
    # Thus, it is most probably 'e'.
    
    # print('XOR'+ str(ord('e') ^ ord('d')))
    #encryption_key = ['x', 'x', 'x']
    #print('XORRY'+ str(ord('g')^ord('G')))
    for keychar in range(ord('a'), ord('z')+1):
        result = ord(' ')^ keychar
        #print(keychar, result)
        if result == 69:
            print(1, chr(keychar))
        if result == 88:
            print(2, chr(keychar))
        if result == 80:
            print(3, chr(keychar))

if __name__ == "__main__":
    Q59()
'''
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
'''