#!/usr/bin/env python3.10

from sys import argv, stdin


def countUpperLetters(string: str) -> int:
    """
    Counts the number of uppercase letters in a given string.

    Args:
        string (str): The input string to be analyzed.

    Returns:
        int: The number of uppercase letters in the input string.
    """
    return sum(1 for c in string if c.isupper())


def countLowerLetters(string: str) -> int:
    """
    Counts the number of lowercase letters in a given string.

    Args:
        string (str): The input string to be analyzed.

    Returns:
        int: The number of lowercase letters in the input string.
    """
    return sum(1 for c in string if c.islower())


def countSpaces(string: str) -> int:
    """
    Counts the number of whitespace characters in a given string.

    Args:
        string (str): The input string to be analyzed.

    Returns:
        int: The number of whitespace characters in the input string.
    """
    return sum(1 for c in string if c.isspace())


def countPunctuation(string: str) -> int:
    """
    Counts the number of punctuation characters in a given string.

    Args:
        string (str): The input string to be analyzed.

    Returns:
        int: The number of punctuation characters found in the input string.

    Example:
        >>> countPunctuation("Hello, world!")
        2
    """
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return sum(1 for c in string if c in punctuation_chars)


def countDigits(string: str) -> int:
    """
    Counts the number of digit characters in a given string.

    Args:
        string (str): The input string to be analyzed.

    Returns:
        int: The number of digit characters found in the input string.
    """
    return sum(1 for c in string if c.isdigit())


def printSummary(string: str) -> None:
    """
    Prints a summary of character counts in the given string.

    The summary includes:
    - Total number of characters
    - Number of uppercase letters
    - Number of lowercase letters
    - Number of punctuation marks
    - Number of spaces
    - Number of digits

    Args:
        string (str): The input string to analyze.

    Returns:
        None
    """
    print(f"""The text contains {len(string)} characters:
    {countUpperLetters(string)} upper letters
    {countLowerLetters(string)} lower letters
    {countPunctuation(string)} punctuation marks
    {countSpaces(string)} spaces
    {countDigits(string)} digits""")


def main():
    """
    Main entry point for the script. Handles command-line arguments and input.

    - If more than one argument is passed, prints an error and exits.
    - If no argument is passed, prompts the user for input via stdin.
    - Otherwise, uses the first argument as the input text.
    - Calls printSummary with the obtained text.

    Exceptions:
        AssertionError: If more than one argument is passed.
        Exception: If reading from stdin fails.
    """
    try:
        assert len(argv) <= 2
    except AssertionError:
        print("AssertionError: more than one argument passed")
        exit(1)

    if len(argv) <= 1:
        print("What is the text to count?")
        try:
            text = stdin.read()
        except Exception:
            text = ""
        if text and text[-1] != '\n':
            print("")
    else:
        text = argv[1]

    printSummary(text)


if __name__ == "__main__":
    main()
