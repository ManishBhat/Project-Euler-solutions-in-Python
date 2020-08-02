# -*- coding: utf-8 -*-
"""
Created on Sun Aug  2 13:31:02 2020

@author: Manish
"""


def fac_arr():
    """Return array with factorials for 0,1 ... 9."""
    fact = [1] * 10
    for n in range(2, 10):
        fact[n] = fact[n-1] * n
    return fact


def digit_fact(n, fact):
    """Compute sum of factorial of digits."""
    sum = 0
    while n != 0:
        sum += fact[n % 10]
        n = int(n/10)
    return sum


def chain(n, memo, fact):
    """Return length of non-repeating digit factorial chain."""
    if n in memo:
        return memo[n]
    ans = digit_fact(n, fact)
    memo[n] = chain(ans, memo, fact) + 1
    return memo[n]


def Q74():
    memo = {1:1, 2:1, 145:1, 40585:1, 169:3, 363601:3, 1454:3, 871: 2, 45361:2, 872:2, 45362:2}
    fact = fac_arr()
    N = 1_000_000
    counter = 0
    for i in range(1, N):
      ans = chain(i, memo, fact)
      if ans == 60:
        counter += 1
    print(counter) # Printing the final answer.

if __name__ == "__main__":
    import time
    start_time = time.time()
    Q74()
    print("Time taken(in s): ", time.time() - start_time)