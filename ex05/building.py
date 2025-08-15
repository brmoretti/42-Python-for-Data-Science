#!/usr/bin/env python3

from sys import argv


def countUpperLetters(string: str) -> int:
    return sum(1 for c in string if c.isupper())


def countLowerLetters(string: str) -> int:
    return sum(1 for c in string if c.islower())


def countSpaces(string: str) -> int:
    return sum(1 for c in string if c.isspace())


def countPunctuation(string: str) -> int:
    punctuation_chars = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
    return sum(1 for c in string if c in punctuation_chars)


def countDigits(string: str) -> int:
    return sum(1 for c in string if c.isdigit())


def printMessage(string: str):
    print(
        f"The text contains {len(string)} characters:\n"
        f"{countUpperLetters(string)} upper letters\n"
        f"{countLowerLetters(string)} lower letters\n"
        f"{countPunctuation(string)} punctuation marks\n"
        f"{countSpaces(string)} spaces\n"
        f"{countDigits(string)} digits"
        )


def main(argv):
    try:
        assert len(argv) <= 2
    except AssertionError:
        print("AssertionError: more than one argument passed")
        exit(1)

    if (len(argv) <= 1 or argv[1] == "None"):
        text = input("What is the text to count?\n")
    else:
        text = argv[1]

    printMessage(text)


if __name__ == "__main__":
    main(argv)
