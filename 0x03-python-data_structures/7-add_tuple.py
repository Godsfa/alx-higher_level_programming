#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    """
    Add two tuples.

    Parameters:
    - tuple_a: The first tuple.
    - tuple_b: The second tuple.

    Returns:
    - A tuple with the addition of corresponding elements from tuple_a and tuple_b.
    """
    # Ensure tuples have at least 2 elements, filling with 0 if necessary
    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    # Sum corresponding elements and create a new tuple
    result_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])

    return result_tuple

# Example usage:
if __name__ == "__main__":
    tuple_a = (1, 2)
    tuple_b = (3, 4)

    result = add_tuple(tuple_a, tuple_b)
    print(f"Tuple A: {tuple_a}")
    print(f"Tuple B: {tuple_b}")
    print(f"Result: {result}")
