#!/usr/bin/python3

def replace_in_list(my_list, idx, element):
    """
    Replace an element of a list at a specific position.

    Parameters:
    - my_list: The original list.
    - idx: The index at which to replace the element.
    - element: The new element to replace at the specified index.

    Returns:
    - The updated list if the replacement is successful, otherwise the original list.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    my_list[idx] = element
    return my_list

# Example usage:
if __name__ == "__main__":
    original_list = [1, 2, 3, 4, 5]

    # Test case to replace element at index 2 with value 10
    updated_list = replace_in_list(original_list, 2, 10)
    print(f"Original List: {original_list}")
    print(f"Updated List: {updated_list}")

    # Test case with a negative index
    negative_index_list = replace_in_list(original_list, -1, 99)
    print(f"List with Negative Index: {negative_index_list}")

    # Test case with an out-of-range index
    out_of_range_index_list = replace_in_list(original_list, 10, 99)
    print(f"List with Out-of-Range Index: {out_of_range_index_list}")
