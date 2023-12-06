def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))

# Example usage:
original_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result_matrix = square_matrix_map(original_matrix)
print(result_matrix)
