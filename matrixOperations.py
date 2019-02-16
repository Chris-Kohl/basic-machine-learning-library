import numpy as np


def idenfunc(x):
    zeroes = np.zeros((x, x))
    for y in range(0, x):
        zeroes[y, y] = 1
    return zeroes


def addNewFeature(x, y):
    ones = np.ones((x.shape[0], 1))
    if y == 0:
        z = np.concatenate((ones, x), axis=1)
    else:
        z = np.concatenate((x, ones), axis=1)
    return z


def dotproduct(x, w):
    return sum(x*w)


def extractResults(x):
    data = x[:, :-1]
    res = x[:, -1]
    return data, res
