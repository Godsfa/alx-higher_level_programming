import numpy as np

def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy's matmul function.

    Args:
    m_a (list of lists of int/float): The first matrix.
    m_b (list of lists of int/float): The second matrix.

    Returns:
    numpy.ndarray: The resulting matrix product of m_a and m_b.

    Raises:
    TypeError: If m_a or m_b is not a list of lists, or if their elements are not integers or floats.
    ValueError: If m_a or m_b is empty, or if the shapes of m_a and m_b are not aligned for multiplication.
    """
    if not isinstance(m_a, list) or not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or not m_b or m_a == [[]] or m_b == [[]]:
        raise ValueError("m_a and m_b can't be empty")
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    return np.matmul(m_a, m_b)