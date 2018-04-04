#!/usr/bin/env python3.5
# Filename: triangle.py

from math import sqrt as sqrt


def user_input():
    """Function returns values list without any whitespace"""    
    triangle = input("name,side1,side2,side3\n")
    triangle = triangle.split(',')
    for i, item in enumerate(triangle):
        triangle[i] = item.strip()
    return triangle


def validator(triangle_data):
    """Return valid data, else raise ValueError"""
    if len(triangle_data) > 4:
        msg = 'Too much parameters'
        raise ValueError(msg)
    elif len(triangle_data) < 4:
        msg = 'Too few parameters'
        raise ValueError(msg)
    for i, item in enumerate(triangle_data[1:], 1):
        msg = "Use positive integers or floating point numbers"
        # check is it number
        if triangle_data[i].replace('.', '', 1).isdigit():            
            triangle_data[i] = float(triangle_data[i])
            # check for zero values
            if triangle_data[i] == 0:
                raise ValueError(msg)
        else:
            raise ValueError(msg)
    return triangle_data


def check_triangle_possible(side1, side2, side3):
    if (sum([side1, side2]) <= side3 or sum([side2, side3]) <= side1 
            or sum([side1, side3]) <= side2):
        msg = 'Triangle cannot exist'
        raise ValueError(msg)

        
def semi_perimeter(side1, side2, side3):
    p = sum([side1 + side2 + side3]) / 2
    return p


def area(side1, side2, side3):
    p = semi_perimeter(side1, side2, side3)
    square = sqrt(p * (p - side1) * (p - side2) * (p - side3))
    return square


def printer(result_list):
    result_list.sort(key=lambda tup: tup[1])
    print("==========Triangle List=========")
    for counter, item in enumerate(result_list):
        print("[Triangle {}]: {:.2f} cm".format(*result_list[counter]))

    
def main():
    result_list = []
    switcher = True
    while switcher:
        triangle_data = user_input()
        valid_values = validator(triangle_data)
        check_triangle_possible(*valid_values[1:])
        name = valid_values[0]
        square = area(*valid_values[1:])
        result_list.append(tuple([name, square]))
        
        answer = input("Do you want input one more triangle?\n").lower()
        if answer != 'y' and answer != 'yes':
            printer(result_list)
            switcher = False

            
if __name__ == '__main__':
    main()
