import sys
from macros import _Flag

"""
Read all options in any.
-s: spaces between numbers in encryption mode's output string.
-v: verbose mode. Useful to desactivate when reusing the
output through pipes, etc.
"""
def _read_options(_i, _argc):
	_argv = sys.argv
	_type = 0

	for _opt in range (1, len(_argv[_i])):
		if _argv[_i][_opt] == 's' or _argv[_i][_opt] == 'v':
			if _argv[_i][_opt] == 's':
				_type |= _Flag.OPTSPACE.value
			elif _argv[_i][_opt] == 'v':
				_type |= _Flag.OPTVERBOSE.value
			else:
				print("Unknown option \'"  + _argv[_i][_opt] + "\'.")
			del _argv[_i]
			_argc -= 1
	return _i, _argc, _type

"""
Check options, encryption (alphabetical) or decryption mode (numeral),
coexistance of letters and numbers.
"""
def _check_argv(_argc, _argv):
	_type = 0

	_i  = 1
	while _i < _argc:
		# Detect options
		if _argv[_i][0] == '-':
			_i, _argc, _type = _read_options(_i, _argc)

		# Only continue if end of array not reached 
		if _i < _argc:
			for _char in _argv[_i]:
				if _char.isdigit():
					_type |= _Flag.NUM.value
				elif _char.isalpha():
					_type |= _Flag.ALPHA.value
				# Return error if both letter and number are used
				if _type & _Flag.NUM.value and _type & _Flag.ALPHA.value:
					_type |= _Flag.ERROR.value
					return _argc, _type
		_i += 1
	return _argc, _type
