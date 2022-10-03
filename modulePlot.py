import math
import matplotlib.pyplot as plt
import numpy as np

M = np.array([[0, 0, 0, 1, 1],
              [1, 0, 0, 0, 1],
              [1, 0, 0, 0, 0],
              [0, 0, 1, 0, 0],
              [0, 0, 1, 0, 0]])



def plot():

    plt.axis([-1, 10, -1, 10])
    x1 = [1, 1, 3] #pour 3 - 1 - 4
    x2 = [1, 5, 1, 5, 5] #pour 3 - 5 - 1 - 2 - 5
    y1 = [1, 4, 6]
    y2 = [1, 4, 4, 1, 4]
    x = x1 + x2
    y = y1 + y2
    plt.plot(x,y, color='r', linestyle='-', marker='o')
    plt.show()
