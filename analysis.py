import math


def maxium_entropy(n_symbols, length):
    entropy = round(length * math.log(n_symbols, 2))

    return entropy


print(maxium_entropy(72, 11))


