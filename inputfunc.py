import numpy as np
import os


def inputfile(fname, separator):
    file = open(fname, 'r')
    datapoints = file.readlines()
    file.close()
    datapoints = [datapoint.replace(separator, ' ') for datapoint in datapoints
                  ]
    file = open('tempdatafile.txt', 'w')
    [file.write(datapoint) for datapoint in datapoints]
    file.close()
    points = np.loadtxt('tempdatafile.txt')
    os.remove('tempdatafile.txt')
    return points
