import math


def maxium_entropy(n_symbols, length):
    entropy = round(length * math.log(n_symbols, 2))

    return entropy


print(maxium_entropy(72, 11))


def almostIncreasingSequence(sequence):
    hasRemoved = False

    for i in range(len(sequence)):
        if i < len(sequence) - 1:
            if constraint_violated(sequence, i) and not hasRemoved:
                hasRemoved = True
                sequence.pop(i + 1)
                if next_is_not_valid(sequence, i):
                    return False
            elif constraint_violated(sequence, i) and hasRemoved:
                return False

    return True


def next_is_not_valid(sequence, i):
    length = len(sequence)

    if i + 1 < length:
        return constraint_violated(sequence, i + 1)
    else:
        return True


def constraint_violated(sequence, i):
    return sequence[i] >= sequence[i + 1]


almostIncreasingSequence([1, 3, 2, 1])