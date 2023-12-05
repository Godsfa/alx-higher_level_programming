#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    """
    Replace an element in a list at a specific position without modifying the original list.

    Parameters:
    - my_list: The original list.
    - idx: The index at which to replace the element.
    - element: The new element to replace at the specified index.

    Returns:
    - A new list with the replacement if idx is valid, otherwise a copy of the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

# Example usage:
if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5]

    # Test case to replace element at index 2 with value 10 without modifying the original list
    updated_list = new_in_list(original_list, 2, 10)
    print(f"Original List: {original_list}")
    print(f"Updated List: {updated_list}")

    # Test case with a negative index (should return a copy of the original list)
    negative_index_list = new_in_list(original_list, -1, 99)
    print(f"List with Negative Index: {negative_index_list}")

    # Test case with an out-of-range index (should return a copy of the original list)
    out_of_range_index_list = new_in_list(original_list, 10, 99)
    print(f"List with Out-of-Range Index: {out_of_range_index_list}")
