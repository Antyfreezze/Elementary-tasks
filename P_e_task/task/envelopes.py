#!/usr/bin/env python3.5
# Filename: converts.py
""" Used python 3.5 """


def validator(check_list):
    if not all(check_list):
        print('Invalid values.\nTry again')
        return
    else:
        for i, item in enumerate(check_list):
            if not (check_list[i].isdigit() and int(check_list[i]) > 0):
                print('Invalid values.\nTry again')
                return
            else:
                check_list[i] = float(check_list[i])        
    return check_list


def area(side1, side2):
    return side1 * side2


def diagonal(side1, side2):
    return side1**2 + side2**2


def perimeter(side1, side2):
    return side1 + side2


def compare(f_height, f_width, s_height, s_width):
    f_area = area(f_height, f_width)
    f_diagonal = diagonal(f_height, f_width)
    f_perimeter = perimeter(f_height, f_width)
    f_short_side = min([f_height, f_width])
    
    s_area = area(s_height, s_width)
    s_diagonal = diagonal(s_height, s_width)
    s_perimeter = perimeter(s_height, s_width)
    s_short_side = min([s_height, s_width])
    
    if (f_area >= s_area) and (f_diagonal >= s_diagonal) and \
            (f_perimeter >= s_perimeter) and (f_short_side >= s_short_side):
        return 'Second can be placed in first'
        
    elif (f_area <= s_area) and (f_diagonal <= s_diagonal) and \
            (f_perimeter <= s_perimeter) and (f_short_side <= s_short_side):
        return 'First can be placed in second'
        
    else:
        return 'Cannot be placed'
        

def main():
    print('Usage: values must be positive integers ',
          'or positive floating-point numbers')    
    play = True
    while play:
        f_height = input('First envelope height: ')
        f_width = input('First envelope width: ')
        s_height = input('Second envelope height: ')
        s_width = input('Second envelope width: ')
        check_list = [f_height, f_width, s_height, s_width]

        # if input is not valid validator will return None
        valid_input = validator(check_list)
        if valid_input:
            print('========== Result ==========')
            print(compare(*valid_input))
        
        answer = input('Do you want play again? ').lower()
        if answer != 'y' and answer != 'yes':
            print('Thank you!')
            play = False

    
if __name__ == "__main__":
    main()    
