#!/usr/bin/python3

def no_c(my_string):
    """
    Remove all occurrences of the characters 'c' and 'C' from a string.

    Parameters:
    - my_string: The input string.

    Returns:
    - The new string with 'c' and 'C' removed.
    """
    filtered_string = ''.join(char for char in my_string if char.lower() not in {'c', 'C'})
    return filtered_string

# Example usage:
if __name__ == "__main__":
    input_string = "Hello World! This is a test string with Cc characters."
    result = no_c(input_string)
    print(f"Original String: {input_string}")
    print(f"String without 'c' and 'C': {result}")
