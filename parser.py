#!/usr/bin/env python3.5
#!Filename: parser.py

import sys

def main():
  mode = 'r'
  sub = ''
  params = len(sys.argv)
  repl = ''
  if params < 2:
    print('Usage: python3.5 parser.py <path to file> <substring to count or replace> <string for replacement>')
    sys.exit(0)
  if params > 2:
    sub = sys.argv[2]
  if params == 4:
    mode = 'w'
    repl = sys.argv[3]
    
  parse(sys.argv[1], mode, sub, repl)

def parse(f_path, mode, sub, repl=''):  
  counter = 0
  #if we need only count substring
  if mode == 'r':
    with open(f_path, mode) as fp:
      for line in fp:
        counter += line.count(sub)
      if counter:    
        print('Counter = {}'.format(counter))
  #if we need make some replacement
  if mode == 'w' and repl != '':
    with open(f_path, 'r') as fp:
      data = fp.read()
      
    with open(f_path, mode) as fp:
      text = data.replace(sub, repl)
      fp.write(text)
      print('Done!')

if __name__ == "__main__":
  main()
  