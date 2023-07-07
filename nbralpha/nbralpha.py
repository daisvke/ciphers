# -*- coding: utf-8 -*-

"""
A numbered alphabet cipher.

During encryption, it takes command-line arguments, convert each argument to a series of numbers representing the position of each character in the alphabet, and prints the results.

The reverse process is done during decryption.
"""

import sys
import re
from unidecode import unidecode

"""
Macros
"""
# Flags
_ALPHA = 1
_NUM = 2
_OPTSPACE = 4
_ERROR = 8

# Colors
_CLR_GREEN = "\033[32m"
_CLR_RESET = "\033[0m"

"""
Letter to number encryption.
"""
def _encrypt(_src, _space_mode):
	for _char in _src:
		# Print non-alphanumerical characters as they are
		if not _char.isdigit() and not _char.isalpha():
			sys.stdout.write(_char)
		elif _char.isalpha():
			_letter = str(ord(_char.upper()) - ord('A') + 1)
			if _space_mode:
				_result = _letter
				_result += " "
			else:
				_result = "0" + _letter if int(_letter) < 10 else _letter 
			sys.stdout.write(_result)

"""
Number to letter decryption.
"""
def _decrypt(_src, _space_mode):
	_src = re.findall(r'\d+|\s{2}|\S', _src)
	print(_src)
	for _number_str in _src:
		# Print non-alphanumerical characters as they are
		if _number_str.isdigit():
			_letter_num = int(_number_str)
			# Range a-z, 
			if (_letter_num >= 1 and _letter_num <= 26) \
				or (_letter_num >= 128 and _letter_num <= 154) \
				or (_letter_num >= 160 and _letter_num <= 165):
				_letter = chr(_letter_num + ord('A') - 1)
				sys.stdout.write(_letter)
		else:
			if _number_str == "  ":
				_number_str = " "
			sys.stdout.write(_number_str)

def _check_argv(_argc, _argv):
	_type = 0

	i  = 1
	while i < _argc:
		# Detect space option
		if _argv[i] == "-s":
			_type |= _OPTSPACE
			del _argv[i]
			_argc -= 1

		# Only continue if end of array not reached 
		if i < _argc:
			for _char in _argv[i]:
				if _char.isdigit():
					_type |= _NUM
				elif _char.isalpha():
					_type |= _ALPHA
				# Return error if both letter and number are used
				if _type & _NUM and _type & _ALPHA:
					_type |= _ERROR
					return _argc, _argv, _type
			i += 1
	return _argc, _argv, _type
		
def _run_encryption_decryption(_arg, _modes):
	_space_mode = _modes & _OPTSPACE
	_encryption_mode = _modes & _ALPHA
	_src_msg = "Original message: " if _encryption_mode \
		else "Encrypted message: "
	_dest_msg = "Encypted message: " if _encryption_mode \
		else "decrypted message: "

	sys.stdout.write(_src_msg)
	print(_arg)
	sys.stdout.write(_dest_msg)
	if _modes & _ALPHA:
		_encrypt(_arg, _space_mode)
	else:
		_decrypt(_arg, _space_mode)

"""
main
"""
_argc = len(sys.argv)

if _argc < 2:
	print("\nUsage: python nbralpha [source],...\n\n"
		"-s: encryption: put spaces between numbers\n")
	sys.exit(1)

_argc, _argv, _modes = _check_argv(_argc, sys.argv)

if _modes & _ERROR:
	print("ERROR: arguments can only contain either digits or letters")
	sys.exit(1)

# Run encryption/decryption
for i in range(1, _argc):
	_arg = _argv[i]
	_run_encryption_decryption(_arg, _modes)
	print("\n")

if _modes & _ALPHA:
	print(_CLR_GREEN + "Encryption complete!" + _CLR_RESET)
else:
	print(_CLR_GREEN + "Decryption complete!" + _CLR_RESET)
