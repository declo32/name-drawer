from matplotlib import pyplot as plt
import numpy as np


def graph(function, x_range):
    x = np.arange(x_range)
    plt.plot(x, function(x))
    plt.show()
