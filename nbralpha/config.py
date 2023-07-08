from enum import Enum

_g_flags = 0

"""
Macros
"""
# Flags
class _Flag(Enum):
	ALPHA = 1
	NUM = 2
	ERROR = 4
	OPTSPACE = 8
	OPTVERBOSE = 16

# Colors
class _Color(Enum):
	GREEN = "\033[32m"
	MAGENTA = "\033[35m"
	RESET = "\033[0m"
