def get_custom_alphabet() -> dict:
    """Return a dictionary containing each character in the following form:
    <ascii char>: <custom alphabet equivalent>

    By default, the custom alphabet supports alphanumeric characters,
    but you can add any character set you like.

    All unhandled characters will remain unencoded in the final output.
    """

    return {
        'A': 'X',
        'B': '8',
        'C': 'Q',
        'D': 'j',
        'E': 'à',
        'F': 'y',
        'G': '^',
        'H': 'ù',
        'I': 's',
        'J': '$',
        'K': 'x',
        'L': 'N',
        'M': 'S',
        'N': 'r',
        'O': 'a',
        'P': '[',
        'Q': 'u',
        'R': 'F',
        'S': '%',
        'T': 'Y',
        'U': '=',
        'V': '2',
        'W': '#',
        'X': 'i',
        'Y': '7',
        'Z': ';',
        '0': '5',
        '1': 'E',
        '2': 'P',
        '3': 'M',
        '4': 'c',
        '5': 'l',
        '6': ':',
        '7': 'U',
        '8': 'q',
        '9': 'p'
        }
