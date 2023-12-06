def multiply_list_map(my_list=[], number=0):
    """
    Returns a new list with all values multiplied by a number.

    Parameters:
    - my_list (list): The input list.
    - number (int): The number to multiply each value.

    Returns:
    - list: A new list with values multiplied by the given number.
    """
    return list(map(lambda x: x * number, my_list))
