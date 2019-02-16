import matplotlib.pyplot as plt
import numpy as np


def plotgraph(x, y):
    plt.plot(x)
    plt.ylabel(y)
    plt.show()


def initWVector(x):
    return np.zeros(x.shape[1])
