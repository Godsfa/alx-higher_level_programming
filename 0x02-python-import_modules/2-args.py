#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    num_args = len(args)

    # Print the number of arguments
    print("{} argument{}{}:".format(
        num_args,
        's' if num_args != 1 else '',
        '' if num_args == 0 else 's'
    ))

    # Print each argument and its position
    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))