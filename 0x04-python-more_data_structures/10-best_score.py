def best_score(a_dictionary):
    """
    Returns the key with the biggest integer value.

    Parameters:
    - a_dictionary (dict): The input dictionary.

    Returns:
    - str or None: The key with the biggest integer value or None if no score found.
    """
    if not a_dictionary:
        # Return None if the dictionary is empty
        return None

    # Find the key with the maximum value
    max_key = max(a_dictionary, key=a_dictionary.get)

    return max_key
