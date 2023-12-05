#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    """
    Print a matrix of integers.

    Parameters:
    - matrix: The matrix of integers.
    """
    for row in matrix:
        for idx, num in enumerate(row):
            if idx == len(row) - 1:
                print("{:d}".format(num))
            else:
                print("{:d}".format(num), end=" ")

# Example usage:
if __name__ == "__main__":
    example_matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    print_matrix_integer(example_matrix)
