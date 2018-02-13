import math


def analyse_password(password):
    n_symbols = count_symbols(password)
    length = len(password)

    entropy  = round(math.log(n_symbols, 2) * length)
    print(entropy)


def count_symbols(password):
    symbols = {}
    total_symbols = 0

    for char in password:
        symbol_set, size = get_symbol_set(char)

        if symbols.get(symbol_set) is None:
            symbols[symbol_set] = size
            total_symbols += size

    return total_symbols


def get_symbol_set(symbol):
    ascii_char = ord(symbol)

    if 33 <= ascii_char <= 47 or 58 <= ascii_char <= 64 or 91 <= ascii_char <= 96 or 123 <= ascii_char <= 126:
        return 'special characters', 32
    elif 48 <= ascii_char <= 57:
        return 'numbers', 10
    elif 54 <= ascii_char <= 90:
        return 'upper case letters', 26
    elif 97 <= ascii_char <= 122:
        return 'lower case letters', 26


if __name__ == "__main__":
    print("Hello!")
    analyse_password("Tr0ub4dor&3")