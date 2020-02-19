#!/usr/bin/python

import argparse

def find_max_profit(prices):
  max_profit = 0
  i = 0
  j = 1

  # if all descending list, subtract smallest from second smallest
  
  negative = 0
  min_difference = prices[0] - prices[1]

  for k in range(1, len(prices)):
    if prices[k] > prices[k - 1]:
      negative += 1
      # capture differences 
    
  if negative == 0:
    for w in range(1, len(prices)):
      if (prices[w -1] - prices[w]) < min_difference:
        
        min_difference = (prices[w-1] - prices[w])
     
    return min_difference * -1
    
  else:
    while j < len(prices):
      if prices[j] < prices[i]:
        i += 1
        j += 1
      elif prices[j] > prices[i]:
        if prices[j] > prices[j - 1]:
          max_profit = prices[j] - prices[i]
          j += 1
        else:
          break
      else:
        break

  return max_profit









if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))