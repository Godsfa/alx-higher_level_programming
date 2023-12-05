#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    """
    Delete the item at a specific position in a list.

    Parameters:
    - my_list: The input list.
    - idx: The index at which to delete the item.

    Returns:
    - The modified list with the item deleted or the same list if idx is negative or out of range.
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return my_list

# Example usage:
if __name__ == "__main__":
    example_list = [1, 2, 3, 4, 5]

    # Delete item at index 2
    result = delete_at(example_list, 2)
    print(f"Original List: {example_list}")
    print(f"Modified List: {result}")

    # Try to delete item at index -1 (should return the same list)
    result_negative_index = delete_at(example_list, -1)
    print(f"List with Negative Index: {result_negative_index}")

    # Try to delete item at index 10 (should return the same list)
    result_out_of_range_index = delete_at(example_list, 10)
    print(f"List with Out-of-Range Index: {result_out_of_range_index}")
