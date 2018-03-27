#!/usr/bin/env python3
#Filename: converts.py
''' Used python 3.5 '''

from math import sqrt as sqrt


def main():
    play = True
    while play:
        valid_input = validator()
        compare(*valid_input)
        answer = input('Do you want play again? ').lower()
        if answer != 'y' and answer != 'yes':
            print('Thank you!')
            play = False


def compare(f_height, f_width, s_height, s_width):
    f_area = f_height * f_width
    f_diagonal = f_height**2 + f_width**2
    f_perimeter = f_height + f_width
    f_short_side = min([f_height, f_width])
    
    s_area = s_height * s_width
    s_diagonal = s_height**2 + s_width**2
    s_perimeter = s_height + s_width
    s_short_side = min([s_height, s_width])
    
    if (f_area >= s_area) and (f_diagonal >= s_diagonal) and \
        (f_perimeter >= s_perimeter) and (f_short_side >= s_short_side):
        print('Second can be placed in first')
        
    elif (f_area <= s_area) and (f_diagonal <= s_diagonal) and \
        (f_perimeter <= s_perimeter) and (f_short_side <= s_short_side):
        print('First can be placed in second')
        
    else:
        print('Cannot be placed')
        
def validator():
    need_validation = True
    print('Usage: values must be positive integers ',
          'or positive floating-point numbers')    
    while need_validation:
        f_height = input('First envelope height: ')
        f_width = input('First envelope width: ')
        s_height = input('Second envelope height: ')
        s_width = input('Second envelope width: ')
        check_list = [f_height, f_width, s_height, s_width]
        
        if not all(check_list):
            print('Invalid values.\nTry again')
        else:
            for i, item in enumerate(check_list):
                if not (check_list[i].isdigit() and int(check_list[i]) > 0):
                    print('Invalid values.\nTry again')
                    break
                else:
                    check_list[i] = float(check_list[i])
                    need_validation = False               
    return check_list
    
if __name__ == "__main__":
    main()

    