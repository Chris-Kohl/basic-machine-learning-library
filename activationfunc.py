from math import exp


def heavisidefunc(x):
    if x >= 0:
        return 1
    else:
        return -1


def sigmoidfunc(a):
    y = 1/1-exp(-a)
    return y
