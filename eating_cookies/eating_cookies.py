#!/usr/bin/python

import sys

# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution

'''
* Since this question is asking you to generate a bunch of possible permutations, you'll probably want to use recursion for this.
 * Think about base cases that we would want our recursive function to stop recursing on. How many ways are there to eat 0 cookies? What about a negative number of cookies? 
 * Once we've established some base cases, how can we recursively call our function such that we move towards one or more of these base cases?
 * As far as performance optimizations go, caching/memoization might be one avenue we could go down? How should we make a cache available to our recursive function through multiple recursive calls?
'''


def eating_cookies(n, cache=None):
  # base case
  # if n = 1, return 1
  if n < 0:
    return 0
  elif n == 0:
    return 1
  elif cache and cache[n]:
    return cache[n]
  else:
    if cache is None:
      cache = {}
    value = eating_cookies(n - 1, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 3, cache)
    cache[n] = value
    return value








if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')