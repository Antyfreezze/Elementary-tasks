#!/usr/bin/env python3
#Filename: converts.py
''' Used python 3.5
    Indentation = 2 spaces '''
from math import sqrt as sqrt

def main():
  play = True
  while play:
    try:
      f_height = float(input('First convert height: '))
      f_width = float(input('First convert width: '))
      s_height = float(input('Second convert height: '))
      s_width = float(input('Second convert width: '))
    except:
      print('Use integets or floating point numbers')
      
    computer(f_height, f_width, s_height, s_width)
    answer = input('Do you want play again? ').lower()
    if answer != 'y' and answer != 'yes':
      print('Thank you!')
      play = False
      
def computer(f_height, f_width, s_height, s_width):
  if f_height <= s_height and f_width <= s_width:
    print('True')
  elif f_height >= s_height and f_width >= s_width:
    print('True')
  else:
    if f_height * f_width > s_height * s_width:
      diag = sqrt(pow(f_height, 2) + pow(f_width, 2))
      if min(s_width, s_height) <= diag - max(s_width, s_height):
        print('True')
      else:
        print('False')
    else:
      diag = sqrt(pow(s_height, 2) + pow(s_width, 2))
      if min(f_width, f_height) <= diag - max(f_width, f_height):
        print('True')
      else:
        print('False')

if __name__ == "__main__":
  main()
    