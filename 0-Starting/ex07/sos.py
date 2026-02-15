from sys import argv


def textToMorse(s: str) -> str:
    """
    Converts a given string to its Morse code representation.

    Parameters:
        s (str): The input string containing alphanumeric characters and
        spaces.

    Returns:
        str: A string representing the input in Morse code, with each
        character separated by a space and words separated by '/'.

    Raises:
        AssertionError: If the input string contains characters that are not
        alphanumeric or spaces.

    Example:
        >>> textToMorse("SOS 123")
        '... --- ... / .---- ..--- ...--'
    """
    NESTED_MORSE = {
        " ": "/",
        "A": ".-",      'B': '-...',    'C': '-.-.',    'D': '-..',
        'E': '.',       'F': '..-.',    'G': '--.',     'H': '....',
        'I': '..',      'J': '.---',    'K': '-.-',     'L': '.-..',
        'M': '--',      'N': '-.',      'O': '---',     'P': '.--.',
        'Q': '--.-',    'R': '.-.',     'S': '...',     'T': '-',
        'U': '..-',     'V': '...-',    'W': '.--',     'X': '-..-',
        'Y': '-.--',    'Z': '--..',
        '0': '-----',   '1': '.----',   '2': '..---',   '3': '...--',
        '4': '....-',   '5': '.....',   '6': '-....',   '7': '--...',
        '8': '---..',   '9': '----.'
    }
    morse_list = []
    for c in s:
        assert c.isalnum() or c.isspace()
        morse_list.append(NESTED_MORSE[c.upper()])
    return " ".join(morse_list)


def main():
    """
    Main function to process command-line input and convert text to Morse code.

    - Expects exactly one command-line argument (excluding the script name).
    - Prints the Morse code translation of the input text.
    - If the input is invalid, prints an error message indicating bad
    arguments.
    """
    try:
        assert len(argv) == 2
        print(textToMorse(argv[1]))
    except AssertionError:
        print(f"{AssertionError.__name__}: the arguments are bad")


if __name__ == "__main__":
    main()
