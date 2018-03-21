import string


def invercaps(text):
    return ''.join(
        c.upper() if c in string.ascii_lowercase
        else c.lower() if c in string.ascii_uppercase
        else c
        for c in text
    )


if __name__ == '__main__':
    print(invercaps('ABCdef'))
    print(invercaps('abcDEF'))
