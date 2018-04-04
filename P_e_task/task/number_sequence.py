#!/usr/bin/env python3.5
# Filename: number_sequence.py


class SequenceGenerator(object):
    """Class for generation sequence of natural numbers"""
    def __init__(self, n):
        self.n = n
        
    def sequence(self):
        i = 0 
        result = []
        while self.n > pow(i, 2):
            result.append(i)
            i += 1
        return str(result)[1:-1]


def validator(number):
    if not number.isdigit():
        print('Use positive integers, please.')
        return
    number = int(number)
    if number <= 0:
        print('Use positive integers, please.')
        return
    else:
        return number

    
def main():
    number = input('Please input top border for sequence:\n')
    valid_value = validator(number)

    if valid_value and valid_value > 0:
        obj = SequenceGenerator(valid_value)
        print(obj.sequence())
    
    
if __name__ == '__main__':
    main()
