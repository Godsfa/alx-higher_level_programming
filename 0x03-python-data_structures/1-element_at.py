#!/usr/bin/python3

def element_at(my_list, idx):
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]

# Example usage:
if __name__ == "__main__":
    my_list = [1, 2, 3, 4, 5]
    
    # Test cases
    index_to_retrieve = 2
    result = element_at(my_list, index_to_retrieve)
    print(f"Element at index {index_to_retrieve}: {result}")

    # Test case with a negative index
    negative_index = -1
    result = element_at(my_list, negative_index)
    print(f"Element at index {negative_index}: {result}")

    # Test case with an out-of-range index
    out_of_range_index = 10
    result = element_at(my_list, out_of_range_index)
    print(f"Element at index {out_of_range_index}: {result}")
