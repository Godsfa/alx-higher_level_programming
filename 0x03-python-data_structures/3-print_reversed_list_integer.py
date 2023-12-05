#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    """
    Print all integers of a list in reverse order.

    Parameters:
    - my_list: The list of integers.

    Format:
    - One integer per line.

    Example:
    - If my_list is [1, 2, 3, 4, 5], the output will be:
      5
      4
      3
      2
      1
    """
    for num in reversed(my_list):
        print("{:d}".format(num))

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    print_reversed_list_integer(my_list)
