# -*- coding: utf-8 -*-

"""
A numbered alphabet cipher.

During encryption, it takes command-line arguments, convert each argument to a series of numbers representing the position of each character in the alphabet, and prints the results.

The reverse process is done during decryption.
"""

import sys
from argv_validation import _check_argv
from cryptography import _encrypt, _decrypt
from macros import _Flag, _Color

"""
Print suitable messages and run encryption or decrpytion.
"""
def _run_encryption_decryption(_arg, _modes):
	_space_mode = _modes & _Flag.OPTSPACE.value
	_encryption_mode = _modes & _Flag.ALPHA.value
	_src_msg = "Original message: " if _encryption_mode \
		else "Encrypted message: "
	_dest_msg = "Encypted message: " if _encryption_mode \
		else "decrypted message: "

	# Print original text
	print("")
	sys.stdout.write(_src_msg)
	print(_arg)

	# Print processed text
	sys.stdout.write(_dest_msg)
	sys.stdout.write(_Color.MAGENTA.value)
	if _modes & _Flag.ALPHA.value:
		_encrypt(_arg, _space_mode)
	else:
		_decrypt(_arg, _space_mode)
	sys.stdout.write(_Color.RESET.value)

"""
main.
"""
_argc = len(sys.argv)

if _argc < 2:
	print("\nUsage: python nbralpha [source],...\n\n"
	"-s: spaces between numbers in encryption mode's output string.\n"
	"-v: verbose mode. Useful to desactivate when reusing the"
	"output through pipes, etc.\n")
	sys.exit(1)

_argc, _modes = _check_argv(_argc, sys.argv)

if _modes & _Flag.ERROR.value:
	print("ERROR: arguments can only contain either digits or letters")
	sys.exit(1)

# Run encryption/decryption
for i in range(1, _argc):
	_arg = sys.argv[i]
	_run_encryption_decryption(_arg, _modes)
	print("\n")

if _modes & _Flag.ALPHA.value:
	print(_Color.GREEN.value + "Encryption complete!" + _Color.RESET.value)
else:
	print(_Color.GREEN.value + "Decryption complete!" + _Color.RESET.value)
