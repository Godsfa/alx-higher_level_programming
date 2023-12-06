def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Parameters:
    - a_dictionary (dict): The input dictionary.
    - key (str): The key to be deleted.

    Returns:
    - dict: The modified dictionary.
    """
    # Check if the key exists before trying to delete
    if key in a_dictionary:
        del a_dictionary[key]

    return a_dictionary
