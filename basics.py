import numpy as np
import matplotlib.pyplot as plt


def idenfunc(x):
    zeroes = np.zeros((x, x))
    for y in range(0, x):
        zeroes[y, y] = 1
    return zeroes


def plotgraph(x, y):
    plt.plot(x)
    plt.ylabel(y)
    plt.show()


def addleftcolumns(x):
    ones = np.ones((x.shape[0], 1))
    y = np.concatenate((ones, x), axis=1)
    return y


def inittheta(x):
    theta = np.ones((1, x.shape[0]))
    return theta


def basichypothesis(x, t):
    theta = t.T
    hypothesis = theta * x
    return hypothesis


def heavisidefunction(x):
    if x >= 0:
        return 1
    else:
        return -1
