import numpy as np
import matplotlib.pyplot as plt

class Visualizer:

    def visualize(self, xdata, b0, b1):
        x_min = np.max(xdata) - 200
        x_max = np.max(xdata) + 200

        x = np.linspace(x_min, x_max)
        y = b1 * x + b0

        plt.plot(x, y, color='#ff0000', label='Linear Regression')

        plt.show()

