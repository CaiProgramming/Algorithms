#!/usr/bin/python

import argparse

def find_max_profit(prices):
    Lowest_num_so_far = prices[0];
    Highest_num_so_far = prices[1];
    Max_num_loc = 1
    max_profit_so_far = Highest_num_so_far - Lowest_num_so_far

    for i in range(1,len(prices)):
        if(Highest_num_so_far < prices[i]):
            Highest_num_so_far = prices[i]
            Max_num_loc = i
    for i in range(0,Max_num_loc):
        if(Lowest_num_so_far > prices[i]):
            Lowest_num_so_far = prices[i]
            max_profit_so_far = Highest_num_so_far - Lowest_num_so_far


    return  max_profit_so_far
if __name__ == '__main__':
  # This is just some code to accept inputs from the command line
  parser = argparse.ArgumentParser(description='Find max profit from prices.')
  parser.add_argument('integers', metavar='N', type=int, nargs='+', help='an integer price')
  args = parser.parse_args()

  print("A profit of ${profit} can be made from the stock prices {prices}.".format(profit=find_max_profit(args.integers), prices=args.integers))
