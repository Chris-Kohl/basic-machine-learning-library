import numpy as np


def badfunc(given, expected):
    y = pow(sum(given-expected), 2)
    return y


def percfunc(w, x, actual, expected):
    range = x.shape[0]
    sum = 0
    t = np.zeros(range)
    for c in range(0, range-1):
        if actual[c] == expected[c]:
            t[c] = 0
        else:
            if x[c] * w < 0:
                t[c] = -1
            else:
                t[c] = 1
        sum += (x[c] * w) * t[c]
    return -sum
