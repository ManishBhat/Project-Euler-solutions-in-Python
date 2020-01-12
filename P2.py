# -*- coding: utf-8 -*-
"""
Created on Wed Dec 25 00:00:47 2019

@author: manis
"""
a1=1
a2=2
sum=0
while(1):
   if a2>4000000:
       break
   elif a2%2==0:
       sum=sum+a2
   temp=a2
   a2=a2+a1
   a1=temp

           