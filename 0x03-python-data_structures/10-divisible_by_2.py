#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    """
    Find all multiples of 2 in a list.

    Parameters:
    - my_list: The input list of integers.

    Returns:
    - A new list with True or False, depending on whether the integer at the same position
      in the original list is a multiple of 2.
    """
    return [num % 2 == 0 for num in my_list]

# Example usage:
if __name__ == "__main__":
    example_list = [1, 2, 3, 4, 5, 6, 7, 8]

    result = divisible_by_2(example_list)
    print(f"Original List: {example_list}")
    print(f"Divisible by 2: {result}")
