def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - dict: A new dictionary with values multiplied by 2.
    """
    # Create a new dictionary with values multiplied by 2
    result_dictionary = {key: value * 2 for key, value in a_dictionary.items()}

    return result_dictionary
