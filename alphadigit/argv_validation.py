import sys
import config

"""
Read all options in any.
-s: spaces between numbers in encryption mode's output string.
-v: verbose mode. Useful to desactivate when reusing the
output through pipes, etc.
"""


def _read_options(_i, _argc):
    _argv = sys.argv

    for _opt in range(1, len(_argv[_i])):
        if _argv[_i][_opt] == 's' or _argv[_i][_opt] == 'v':
            if _argv[_i][_opt] == 's':
                config._g_flags |= config._Flag.OPTSPACE.value
            elif _argv[_i][_opt] == 'v':
                config._g_flags |= config._Flag.OPTVERBOSE.value
        elif config._g_flags & config._Flag.OPTVERBOSE.value:
            print("Unknown option \'" + _argv[_i][_opt] + "\'.")
    del _argv[_i]
    _argc -= 1
    return _i, _argc


def _check_argv(_argc, _argv):
    """
    Check options, encryption (alphabetical) or decryption mode (numeral),
    coexistance of letters and numbers.
    """
    _i = 1
    while _i < _argc:
        # Detect options
        if _argv[_i][0] == '-':
            _i, _argc = _read_options(_i, _argc)

        # Only continue if end of array not reached
        if _i < _argc:
            for _char in _argv[_i]:
                if _char.isdigit():
                    config._g_flags |= config._Flag.NUM.value
                elif _char.isalpha():
                    config._g_flags |= config._Flag.ALPHA.value
                # Return error if both letter and number are used
                if (config._g_flags & config._Flag.NUM.value
                        and config._g_flags & config._Flag.ALPHA.value):
                    config._g_flags |= config._Flag.ERROR.value
                    return _argc
        _i += 1
    return _argc
