#!/usr/bin/env python3
#Filename: triangle.py

from math import sqrt as sqrt


def main():
    triangle_dict = {}
    more = True
    while more:  
        try:
            triangle_name = input('Input, please, name of triangle: ')
            print('Input, please, sides of triangle:')
            a = float(input('a = '))
            b = float(input('b = '))
            c = float(input('c = '))
        except:
            print('Use integers or floating point numbers')
            break
      
        if not((a + b > c) and (a + c > b) and (b + c > a)):
            print('Wow! Such triangle cannot exist!')
        else:
            #p - 1/2 perimeter
            s = square(a, b, c)
            triangle_dict[s] = triangle_name
  
        answer = input('Do you want add one more triangle? ').lower()
        if answer != 'y' and answer != 'yes':
            print('Thank you!')
            if triangle_dict:
            print('===========Triangle list===========')
        square_list = list(triangle_dict.keys())
        for k in sorted(square_list):
            print('[Triangle {}] {:.2f} cm'.format(triangle_dict.get(k), k))
            more = False

def square(a, b, c):
    p = (a + b + c)/2
    s = sqrt(p * (p - a) * (p - b) * (p - c))
    return s

if __name__ == '__main__':
    main()
  