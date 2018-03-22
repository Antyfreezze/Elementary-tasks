#!/usr/bin/env python3.5
#Filename: ticket.py

import sys
import string
def main():

  if len(sys.argv) < 2:
    print('Usage: python3 ticket.py <path_to_file>')
    print('Use 6digit number')
    print('Try again.')
    sys.exit(1)
    
  reader(sys.argv[1])  
  count = stupid_brut()
  print(count)

def reader(path_to_file):
  with open(path_to_file,'r') as fp:
    for line in fp:
      line = line.lower()
      if line.count('piter'):
        print('Use Piter variant')
        break
      elif line.count('moscow'):
        print('Use Moscow variant')
        break      
  
def stupid_brut():
  count = 0
  y = 0
  a = 0
  b = 999999
  while a <= b-1:

      y = str.zfill(str(a),6)
      c = y[0]
      c1 = y[1]
      c2 = y[2]
      d = y[3]
      d1 = y[4]
      d2 = y[5]
      a+=1

      if int(c)+ int(c1)+ int(c2) == int(d)+int(d1)+ int(d2):
          count+=1

  return count

if __name__ == '__main__':
  main()
  
