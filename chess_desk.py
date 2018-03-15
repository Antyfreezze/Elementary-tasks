#!/usr/bin/env python3
#Filename: chess_desk.py
''' Programm for printing chess field by height and width which controlled by user.
    Used python 3.5
    Indentation = 2 spaces'''
import sys

def main():
  mistake = True
  while mistake == True:
    user_height = input('Please input height value ')
    user_width = input('Please input width value ')

    if user_height == 'q' or user_width == 'q':
      sys.exit(1)

    try:
      height = int(user_height)
      width = int(user_width)
      mistake = False
    except:
      print('Use integers for width and height or "q" to leave')
      
    field = FieldGenerator(height, width)
    print(field.string_concat())   
    
class FieldGenerator:
  ''' Class for creation chess field '''
  def __init__(self, height, width):
    self.height = height
    self.width = width

  def string_concat(self):
    result = ''
    first_string = '* ' * self.width + '\n'
    second_string = ' *' * self.width + '\n'
    for i in range(self.height):
      if i % 2 ==0:
        result += first_string
      else:
        result += second_string  
    return result    

if __name__ == "__main__":
  main()
  