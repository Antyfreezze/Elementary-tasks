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
      
def computer(a, b, c, d):
  if ( (a * b  >= c * d) and ( (a**2 + b**2) >= (c**2 + d**2) ) and
                    (a + b >= c + d) and ( min(a, b) >= min(c, d) ) ):
    print('Second in first')
  elif ( (a * b  <= c * d) and ( (a**2 + b**2) <= (c**2 + d**2) ) and
                    (a + b <= c + d) and ( min(a, b) <= min(c, d) ) ):
    print('First in second')
  else:
    print('Cannot be placed')
    
if __name__ == "__main__":
  main()
    