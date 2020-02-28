# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 02:19:09 2020

@author: manis
"""

#Much more beautiful solution is to simply observe 1/7 =0.(142857) has the
#permutation property due to being infinitely repeating

def main():
    x=2
    while True:
        if ''.join(sorted(str(x)))==''.join(sorted(str(2*x))):
            if ''.join(sorted(str(x)))==''.join(sorted(str(3*x))):
                if ''.join(sorted(str(x)))==''.join(sorted(str(4*x))):
                    if ''.join(sorted(str(x)))==''.join(sorted(str(5*x))):
                        if ''.join(sorted(str(x)))==''.join(sorted(str(6*x))):
                            print(x)
                            break
        x+=1

if __name__ == '__main__':
    import time
    start_time = time.time()
    main()
    print("Program run time(in s): ", (time.time() - start_time))    