#!/usr/bin/env python3
# Filename: fibo.py
""" Used python 3.5
    Indentation = 2 spaces """

import sys


class Fibo(object):
    def __init__(self, low, high):
        self.low = low
        self.high = high
        self.res_list = [0, 1]

    def fibo_sequence(self):
        a = 0
        b = 1
        i = 2
        while i < self.high:
            temp = a + b
            a = b
            b = temp
            i += 1
            self.res_list.append(temp)
        return self.res_list

    def fibo_shape(self):
        self.fibo_sequence()
        if self.low > 0:
            self.low -= 1
        res_str = str(self.res_list[self.low: self.high])[1:-1]
        return res_str


def main():
    try:
        low = int(input('Input low border: '))
        high = int(input('Input top border: '))
        if high < low:
            high, low = low, high
        if low <= 0 or high <= 0:
            print('Use positive integers, please')
    except ValueError:
        print('Use integers, please')
        sys.exit(1)
    obj = (Fibo(low, high))
    print(obj.fibo_shape())    
  
  
if __name__ == '__main__':
    main()
