#!/usr/bin/python3
import sys

if __name__ == "__main__":
    args = sys.argv[1:]

    # Sum all the arguments (converted to integers)
    result = sum(int(arg) for arg in args)

    # Print the result
    print(result)
