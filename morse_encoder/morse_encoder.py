#!/usr/bin/env python3

from sys import stderr
from argparse import ArgumentParser, Namespace
from morse_dict import get_alnum_to_morse, get_morse_to_alnum


class MorseEncoder:
    """
    The program takes a string as an argument and encodes it
    into Morse Code, and vice versa.

    It supports space and alphanumeric characters.
    Complete morse characters are separated by a single space.
    A space character is represented by a slash '/'.
    """

    def __init__(
            self,
            string_to_convert: str,
            morse_to_alnum: bool
            ):
        self.string_to_convert: str = string_to_convert
        self.morse_to_alnum: bool = morse_to_alnum
        self.alnum_to_morse_dict: dict = get_alnum_to_morse()
        self.morse_to_alnum_dict: dict = get_morse_to_alnum()

    def convert_from_alnum_to_morse(self):
        # Check if all characters are handled
        for char in self.string_to_convert:
            if not char.isalnum() and char != ' ':
                raise AssertionError("Text contains unhandled character(s).")

        morse = self.alnum_to_morse_dict  # Get the Morse Code dictionary
        string_len = len(self.string_to_convert) - 1

        # enumerate() gives the current index and the character
        for i, char in enumerate(self.string_to_convert):
            if (i != string_len):  # If not the last char
                print(morse[char.upper()], end="")
            else:  # Don't print the space after the last Morse character
                print(morse[(char.upper())][:-1])

    def convert_from_morse_to_alnum(self):
        # Get Morse chars from the string into an array (separator = space)
        morse_chars = self.string_to_convert.split(" ")
        morse = self.morse_to_alnum_dict  # Get the Morse Code dictionary

        # Check if all characters are handled
        for char in morse_chars:
            char = char + ' '
            if char not in morse:
                raise AssertionError("Text contains unhandled character(s).")
            print(morse[char], end="")


def parse_args() -> Namespace:
    """
    Parse command-line arguments.
    """
    # Create the parser
    parser = ArgumentParser(description="""Convert a string into Morse code,
                            or vice versa,
                            handling space and alphanumeric characters with a
                            dictionary lookup.
                            """)

    # Add arguments
    parser.add_argument(
        'string', type=str, help='the text to convert'
        )
    parser.add_argument(
        '-r', '--reverse', action='store_true',
        help="Convert from Morse code to alphanumerical string")

    return parser.parse_args()


def main():
    args = parse_args()

    morseEncoder = MorseEncoder(args.string, args.reverse)

    if not args.reverse:
        args.reverse = False

    if args.reverse:
        morseEncoder.convert_from_morse_to_alnum()
    else:
        morseEncoder.convert_from_alnum_to_morse()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"AssertionError: {e}", file=stderr)
