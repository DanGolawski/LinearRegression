import numpy as np
import matplotlib.pyplot as plt

class Visualizer:

    def visualize(self, xdata, ydata, b0, b1):
        # plotting values
        x_max = np.max(xdata) + 100
        x_min = np.min(xdata) - 100

        # calculating line values of x and y
        x = np.linspace(x_min, x_max, 1000)
        y = b0 + b1 * x

        # plotting line
        plt.plot(x, y, color='#00ff00', label='Linear Regression')

        # plot the data point
        plt.scatter(xdata, ydata, color='#ff0000', label='Data Point')

        # x-axis label
        plt.xlabel('Head Size (cm^3)')
        # y-axis label
        plt.ylabel('Brain Weight (grams)')

        plt.legend()

        plt.show()

