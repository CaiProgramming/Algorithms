#!/usr/bin/python

import sys

def rock_paper_scissors(n):
  if n == 0:
    return [[]]

  result = []
  players= [0]*n

  permutations_rps(players,0, result)
  return result


def permutations_rps(arr,index, result):
    if index == len(arr):
        result.append(list(arr))
        return arr

    for v in ("rock","paper","scissors"):
        arr[index] =v
        permutations_rps(arr,index+1, result)

if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
