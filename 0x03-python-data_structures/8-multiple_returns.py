#!/usr/bin/python3

def multiple_returns(sentence):
    """
    Return a tuple with the length of a string and its first character.

    Parameters:
    - sentence: The input string.

    Returns:
    - A tuple with the length of the string and its first character.
    """
    if not sentence:
        return (0, None)

    length = len(sentence)
    first_char = sentence[0]

    return (length, first_char)

# Example usage:
if __name__ == "__main__":
    example_sentence = "Hello, World!"

    result = multiple_returns(example_sentence)
    print(f"Sentence: {example_sentence}")
    print(f"Result: {result}")
