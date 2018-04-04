#!/usr/bin/env python3.5
# Filename: parser.py

import sys


def parse(f_path, mode, sub, repl=''):
    counter = 0
    # if we need only count substring
    if mode == 'r':
        with open(f_path, mode) as fp:
            for line in fp:
                counter += line.count(sub)
                if counter:
                    print('Counter = {}'.format(counter))
    # if we need make some replacement
    if mode == 'w':
        with open(f_path, 'r') as fpointer:
            data = fpointer.read()

        with open(f_path, mode) as fpointer:
            text = data.replace(sub, repl)
            fpointer.write(text)
        print('Done!')


def main():
    mode = 'r'
    sub_str = ''
    params = len(sys.argv)
    repl = ''
    if params < 2:
        print('Usage: python3 parser.py <path to file> '
              '<substring to count or replace> [<string for replacement>]')
        sys.exit(0)
    if params > 2:
        sub_str = sys.argv[2]
    if params == 4:
        mode = 'w'
        repl = sys.argv[3]

    parse(sys.argv[1], mode, sub_str, repl)


if __name__ == "__main__":
    main()
