#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A numbered alphabet cipher.

During encryption, it takes command-line arguments, convert each argument to a series of numbers representing the position of each character in the alphabet, and prints the results.

The reverse process is done during decryption.
"""

from sys import stderr
import sys
import config
from argv_validation import _check_argv
from cryptography import _encrypt, _decrypt

"""
Print suitable messages and run encryption or decrpytion.
"""


def _run_encryption_decryption(_arg):
    _space_mode = config._g_flags & config._Flag.OPTSPACE.value
    _encryption_mode = config._g_flags & config._Flag.ALPHA.value
    _src_msg = "Original message: " if _encryption_mode \
        else "Encrypted message: "
    _dest_msg = "Encypted message: " if _encryption_mode \
        else "decrypted message: "

    # Print original text if in verbose mode
    if (config._g_flags & config._Flag.OPTVERBOSE.value):
        print("")
        sys.stdout.write(_src_msg)
        print(_arg)
    # Print processed text if in verbose mode
        sys.stdout.write(_dest_msg)
        sys.stdout.write(config._Color.MAGENTA.value)

    # Process data
    if config._g_flags & config._Flag.ALPHA.value:
        _encrypt(_arg)
    else:
        _decrypt(_arg)

    # Reset color
    if (config._g_flags & config._Flag.OPTVERBOSE.value):
        sys.stdout.write(config._Color.RESET.value)


def main():
    _argc = len(sys.argv)

    if _argc < 2:
        print("\nUsage: ./alphadigit [source],...\n\n"
        "-s: spaces between numbers in encryption mode's output string.\n"
        "-v: verbose mode. Useful to desactivate when reusing the "
        "output through pipes, etc.\n")
        sys.exit(1)

    _argc = _check_argv(_argc, sys.argv)
    if config._g_flags & config._Flag.ERROR.value:
        print(
            "ERROR: Arguments can only contain either all digits or all"
            " letters, but not both."
            )
        sys.exit(1)

    # Run encryption/decryption
    for i in range(1, _argc):
        _arg = sys.argv[i]
        _run_encryption_decryption(_arg)
        if config._g_flags & config._Flag.OPTVERBOSE.value:
            print("\n")

    if config._g_flags & config._Flag.OPTVERBOSE.value:
        if config._g_flags & config._Flag.ALPHA.value:
            print(config._Color.GREEN.value + "Encryption complete!" + \
                config._Color.RESET.value)
        else:
            print(config._Color.GREEN.value + "Decryption complete!" + \
                config._Color.RESET.value)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(f"Error: {e}", file=stderr)
