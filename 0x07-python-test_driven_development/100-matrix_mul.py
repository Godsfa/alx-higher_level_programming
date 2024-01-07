def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices and returns the result.

    Args:
    m_a (list of lists of int/float): The first matrix.
    m_b (list of lists of int/float): The second matrix.

    Raises:
    TypeError: If m_a or m_b is not a list of lists.
    ValueError: If m_a or m_b is empty or if they cannot be multiplied.
    """
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if not all(all(isinstance(elem, (int, float)) for elem in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("each row of m_a must be of the same size")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    result = []
    for i in range(len(m_a)):
        result_row = []
        for j in range(len(m_b[0])):
            sum = 0
            for k in range(len(m_b)):
                sum += m_a[i][k] * m_b[k][j]
            result_row.append(sum)
        result.append(result_row)

    return result