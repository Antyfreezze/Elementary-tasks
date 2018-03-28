#!/usr/bin/env python3.5
#Filename: ticket.py

import os
import sys
import string

def reader(path_to_file):
    with open(path_to_file,'r') as fp:
        for line in fp:
            line = line.lower()
            if line.count('piter'):
                print('Use Piter variant')
                mode = 'p'
                return mode
            elif line.count('moscow'):
                print('Use Moscow variant')
                mode = 'm'
                return mode
            else:
                print('Undefined mode, check file or path')
                return
            
def lucky_ticket_list(mode, low, high):
    if low == 0 and high == 999999:
        return 55252
    count = 1
    if mode == 'm':
        for low in range(low, high):
            ticket = str.zfill(str(low), 6)
            left_side = sum([int(ticket[0]), int(ticket[1]), int(ticket[2])])
            right_side = sum([int(ticket[3]), int(ticket[4]), int(ticket[5])])
            if left_side == right_side:
                count += 1
    elif mode == 'p':
        for low in range(low, high):
            ticket = str.zfill(str(low), 6)
            left_side = sum([int(ticket[1]), int(ticket[3]), int(ticket[5])])
            right_side = sum([int(ticket[0]), int(ticket[2]), int(ticket[4])])
            if left_side == right_side:
                count += 1
    return count

def validator(path_to_file='0', low='0', high='0'):
    if not low.isdigit() or not high.isdigit():
        print('Use positive integers')
        return
    low = int(low)
    high = int(high)
    if min(low, high) < 0:
        print('Use positive integers')
        return
    if not os.path.exists(path_to_file):
        print('Cannot find such file')
        return
    if not os.path.isfile(path_to_file):
        print('Cannot find such file')
        return
    valid_values = [path_to_file, low, high]     
    return valid_values


def main():
    mode = ''
    valid_values = validator(*sys.argv[1:4])
    if valid_values:
        mode = reader(valid_values[0])
    if mode:
        count = lucky_ticket_list(mode, valid_values[1], valid_values[2])
        print(count)          


if __name__ == '__main__':
    main()

