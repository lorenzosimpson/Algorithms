#!/usr/bin/python

import sys


def rock_paper_scissors(n):
  options = ['rock', 'paper', 'scissors']
  all_possibilities = []

  def rps_helper(result, rounds):
    if rounds == 0:
      all_possibilities.append(result)
      return
    for i in range(0, len(options)):
      rps_helper(result + [options[i]], rounds - 1)
  
  rps_helper([], n)
  return all_possibilities


print(rock_paper_scissors(2))















if __name__ == "__main__":
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')