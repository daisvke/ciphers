import sys
import re

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
			# Add 0 in front of the digit
			if not _space_mode:
				_result = "0" + _letter if int(_letter) < 10 else _letter 
			sys.stdout.write(_letter)
		if _space_mode:
			sys.stdout.write(" ")

def _is_punctuation(_src):
	return _src == "!" or _src == "." or _src == ":" \
		or _src == ";" or _src == "?"

"""
Number to letter decryption.
"""
def _decrypt(_src, _space_mode):
	# Split the argument string
	_src = re.findall(r'\d+|\s{2}|\W', _src)
	for index, _number_str in enumerate(_src):
		# Print non-alphanumerical characters as they are
		if _number_str.isdigit():
			_letter_num = int(_number_str)
			# Ranges: a-z, Ç-Ü, á-Ñ
			if (_letter_num >= 1 and _letter_num <= 26) \
				or (_letter_num >= 128 and _letter_num <= 154) \
				or (_letter_num >= 160 and _letter_num <= 165):
				_letter = chr(_letter_num + ord('A') - 1)
				sys.stdout.write(_letter)
		elif (_number_str == " " and _is_punctuation(_src[index -1])) or \
				_number_str == "  ":
				sys.stdout.write(" ")
		elif _number_str != " ":
			sys.stdout.write(_number_str)
