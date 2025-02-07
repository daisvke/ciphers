#!/usr/bin/env python3

from sys import stderr
from argparse import ArgumentParser, Namespace
import json


class Alphabet:
    """
    The program takes a string as an argument and encodes or decodes it
    according to our custom alphabet.

    By default, the custom alphabet supports alphanumeric characters,
    but you can add any character set you like.

    All unhandled characters will remain unencoded in the final output.
    """

    def __init__(
            self,
            string_to_convert: str,
            alphabet_dict: dict,
            encoded_to_original: bool
            ):

        # Check if all characters in the given text are printable
        if not string_to_convert.isprintable():
            raise AssertionError("Text contains non printable character(s).")

        self.string_to_convert: str = string_to_convert
        self.alphabet_dict: dict = alphabet_dict
        # Convert an encoded text to the original text
        self.encoded_to_original: bool = encoded_to_original

    def convert_from_original_to_encoded(self) -> None:
        alphabet = self.alphabet_dict  # Get the custom alphabet dictionary

        for char in self.string_to_convert:
            upper_char = char.upper()
            if upper_char in alphabet:
                print(alphabet[upper_char], end="")
            else:
                for standard, custom in alphabet.items():
                    """
                    If the character isn't handled but exists as a custom
                    character, we raise an error as it would lead to a
                    conversion error when decoding to the original text.

                    Ex.:
                        alphabet = {'A': '.'}
                        string_to_convert = "."

                        // If we decide to leave the dot in the output
                        "." => encode => "."
                        // Then, when decoding
                        "." => decode => "A" != string_to_convert
                    """

                    if char == custom:
                        raise AssertionError(
                            "Text contains unhandled character(s)."
                            )
                # If the character is not found in the alphabet
                print(char, end="")  # Print the unencoded character

    def convert_from_encoded_to_original(self) -> None:
        alphabet = self.alphabet_dict  # Get the custom alphabet dictionary

        for char in self.string_to_convert:
            found = False
            for standard, custom in alphabet.items():
                # If we find the character in the custom alphabet, we print
                # the corresponding character from the standard alphabet
                if char == custom:
                    print(standard, end="")
                    found = True
                    break
            # If the character is not found in the alphabet
            if not found:
                print(char, end="")  # Print the undecoded character


def parse_args() -> Namespace:
    """
    Parse command-line arguments.
    """
    # Create the parser
    parser = ArgumentParser(
        description="""
            The program takes a string as an argument and encodes or decodes
            it according to our custom alphabet.

            By default, the custom alphabet supports alphanumeric characters,
            but you can add any character set you like.

            All unhandled characters will remain unencoded in the final output.
            """)

    # Add arguments
    parser.add_argument(
        'string_to_convert', type=str, help='the text to convert'
        )
    parser.add_argument(
        'alphabet_dict',
        type=str,
        help='JSON file containing the custom alphabet'
        )

    parser.add_argument(
        '-r', '--reverse', action='store_true',
        help="convert an encoded text to the original text")

    return parser.parse_args()


def main():
    args = parse_args()

    # Open the file and load the dictionary
    with open(args.alphabet_dict, 'r') as file:
        alphabet_dict = json.load(file)

    if not alphabet_dict:
        raise AssertionError("Alphabet dictionary is empty!")

    encoder = Alphabet(
            args.string_to_convert,
            alphabet_dict,
            args.reverse
        )

    if args.reverse:
        encoder.convert_from_encoded_to_original()
    else:
        encoder.convert_from_original_to_encoded()


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=stderr)
