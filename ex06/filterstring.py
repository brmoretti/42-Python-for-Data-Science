#!/usr/bin/env python3.10

from sys import argv
from ft_filter import ft_filter


def containsSpecialCharacters(s):
    """
    Returns True if the string contains any special characters
    (punctuation or invisible/whitespace except space), else False.
    """
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return any(
        c in punctuation_chars or (c.isspace() and c != ' ')
        for c in s
    )


def main():
    """
    Filters and prints words from the first command-line argument whose length
    is greater than the integer argument.

    - Expects exactly two arguments: a string of words and an integer.
    - Raises an AssertionError if:
        - The number of arguments is not exactly two.
        - The second argument cannot be converted to an integer.
        - Any word contains special characters (as determined by
        containsSpecialCharacters).
    - Splits the first argument into words and filters out those with length
    less than or equal to the integer.
    - Prints the filtered list of words.
    - Prints an AssertionError message if arguments are missing or invalid.
    """
    try:
        if len(argv) != 3:
            raise AssertionError("the arguments are bad")
        try:
            n = int(argv[2])
            for s in argv[1]:
                if containsSpecialCharacters(s):
                    raise AssertionError("the argument contains"
                                         " a special character")
            words = argv[1].split()
            print(list(ft_filter(lambda s: len(s) > n, words)))
        except ValueError:
            raise AssertionError("the arguments are bad")
    except AssertionError as e:
        print(f"{AssertionError.__name__}: {e}")


if __name__ == "__main__":
    main()
