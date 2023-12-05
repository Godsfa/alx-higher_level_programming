#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the biggest integer in a list.

    Parameters:
    - my_list: The input list of integers.

    Returns:
    - The biggest integer in the list, or None if the list is empty.
    """
    if not my_list:
        return None

    max_num = my_list[0]
    for num in my_list:
        if num > max_num:
            max_num = num

    return max_num

# Example usage:
if __name__ == "__main__":
    example_list = [4, 2, 8, 1, 5, 7]

    result = max_integer(example_list)
    print(f"List: {example_list}")
    print(f"Max Integer: {result}")
