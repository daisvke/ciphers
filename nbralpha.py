"""
A numbered alphabet cipher.

It takes command-line arguments, convert each argument to a series of numbers representing the position of each character in the alphabet, and prints the results.
"""

import sys

_ALPHA = 1
_NUM = 2
_OPTSPACE = 4

# Letter to number encryption.
def _encrypt(_src, _space_mode):
	for _char in _src:
		if _char != ' ':
			_letter = str(ord(_char.upper()) - ord('A') + 1)
			if _space_mode:
				_result = _letter
				_result += " "
			else:
				_result = "0" + _letter if int(_letter) < 10 else _letter 
			sys.stdout.write(_result)
	print("")

# Number to letter decryption.
def _decrypt(_src, _space_mode):
	for _char in _src:
		_result = str(ord(_char.upper()) + ord('A') - 1)
		sys.stdout.write(_result)

def _check_argv(_argc, _argv):
	_type = 0

	for i in range(1, _argc):
		# Detect space option
		if _argv[i] == "-s":
			_type |= _OPTSPACE
			del _argv[i]
			if i + 1 < _argc:
				_argv[i] = _argv[i + 1]
			_argc -= 1
			continue
		for _char in _argv[i]:
			if _type & _ALPHA == 0 and _char.isdigit():
				_type |= _NUM
			elif _type & _NUM == 0 and _char.isalpha():
				_type |= _ALPHA
			elif _char != ' ':
				return -1
	return _argc, _argv, _type
		

_argc = len(sys.argv)

if _argc < 2:
	print("Usage: python nbralpha [source]")
	sys.exit(1)

_argc, _argv,_mode = _check_argv(_argc, sys.argv)
_space_mode = _mode & _OPTSPACE

if _mode == -1:
	print("ERROR")
	sys.exit(1)

for i in range(1, _argc):
	_arg = sys.argv[i]
	sys.stdout.write("\'")
	sys.stdout.write(_arg)
	sys.stdout.write("\' => ")
	if _mode & _ALPHA:
		_encrypt(_arg, _space_mode)
	else:
		_decrypt(_arg, _space_mode)
