import numpy as np
import matplotlib.pyplot as plt


def plotgraph(x, y):
    plt.plot(x)
    plt.ylabel(y)
    plt.show()


def initialiseweights(x):
    theta = np.ones((1, x.shape[0]))
    return theta


def calcA(x, t):
    theta = t.T
    hypothesis = theta * x
    return hypothesis
