#!/usr/bin/python

import sys


def eating_cookies(n, cache=None):
  if n < 0:
    return 0
  elif n == 0:
      return 1
  return eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')




# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
def eating_cookies(n, cache=None):
  if cache is None or type(cache) == list: # this will overwrite the array cache and replace with a dictionary cache
    cache = {0:1, 1:1, 2:2, 3:4}
  if n < 0:
    return 0
  elif n not in cache:
    # another way of doing it but more steps and slower
    # cache[n] = eating_cookies(n - 3) + eating_cookies(n - 2) + eating_cookies(n - 1)
    cache[n] = eating_cookies(n - 3, cache) + eating_cookies(n - 2, cache) + eating_cookies(n - 1, cache)
  return cache[n]

print(eating_cookies(10))
