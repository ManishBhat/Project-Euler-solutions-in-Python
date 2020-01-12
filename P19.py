# -*- coding: utf-8 -*-
"""
Created on Sat Jan 11 22:10:06 2020

@author: manis
"""

def leapYear(n):
    if n%4!=0:
        return False
    elif n%100!=0:
        return True
    elif n%400!=0:
        return False
    else:
        return True

a=['Sun','Mon','Tue','Wed','Thu','Fri','Sat']
NoOfDays=100000
year=1900
dayofYear=1
dayofMonth=1
month=1
Date=1
sundays=0
for i in range(NoOfDays):
    if(dayofMonth==1 and month==1 and year==1901):
        sundays=0
    if(dayofMonth==1 and Date==0):
        sundays=sundays+1
    if(dayofMonth==31 and month==12 and year==2000):
        #print('Help')
        break
    #print(dayofMonth,month,year,a[Date])
    if (dayofYear==365 and leapYear(year)==False) or (dayofYear==366 and leapYear(year)==True):
        #print('Hi-1')
        Date=(Date+1)%7
        dayofYear=1
        dayofMonth=1
        month=1
        year=year+1
        i=i+1
    elif dayofMonth==31 and (month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12):
        #print('Hi-2')
        Date=(Date+1)%7
        dayofYear=dayofYear+1
        dayofMonth=1        
        month=month+1
        i=i+1
    elif dayofMonth==30 and (month==4 or month==6 or month==9 or month==11):
        #print('Hi-3')
        Date=(Date+1)%7
        dayofYear=dayofYear+1
        dayofMonth=1
        month=month+1
        i=i+1        
    elif (dayofMonth==28 and month==2 and leapYear(year)==False) or (dayofMonth==29 and month==2 and leapYear(year)==True):
        #print('Hi-4')
        Date=(Date+1)%7
        dayofYear=dayofYear+1
        dayofMonth=1
        month=month+1
        i=i+1
    else:
        #print('Hi-5')
        Date=(Date+1)%7
        dayofYear=dayofYear+1
        dayofMonth=dayofMonth+1
        i=i+1
print(sundays)