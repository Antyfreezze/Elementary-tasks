#!/usr/bin/env python3
#Filename: number_sequence.py
''' Used python 3.5
    Indentation = 2 spaces '''

import sys

def main():
  try:
    n = int(input('Please input top border for sequence:\n'))
  except:
    print('Use integers, please.')
    sys.exit(1)

  obj = SequenceGenerator(n)
  print(obj.sequence())
    
    
class SequenceGenerator():
  ''' Class for generation sequence of natural numbers '''
  def __init__(self, n):
    self.n = n
    
  def sequence(self):
    i = 0
    result = []
    while self.n > pow(i, 2):
      result.append(i)
      i += 1
    return str(result)[1:-1]
  
    
if __name__ == '__main__':
  main()
  