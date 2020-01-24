#!/usr/bin/python

import argparse

def find_max_profit(prices):
  # find max value
  max_profit = 0
  max_index = (prices.index(max(prices))) # finding index of the max value in list
  if max_index == 0: 
    new_arr_minus_max = prices[1:] # making a new list if the maximum value is in index[0]
    max_index_new = max(new_arr_minus_max) # max of new list (new_arr_minus_max)
    if max_index_new is new_arr_minus_max[0]: # if that new max is in index[0] of new array
      return (max_index_new - max(prices)) # new list max - the max of the old list
    else: 
      return (max(new_arr_minus_max) - min(new_arr_minus_max)) # new list max - new list min
  else:
    # split the array left and right (where the biggest value is)
    new_arr = prices[0:max_index + 1]
    return (max(new_arr) - min(new_arr))

    
#print(find_max_profit([10, 7, 5, 8, 11, 9]))
# print(find_max_profit([100, 90, 80, 50, 20, 10]))


if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))