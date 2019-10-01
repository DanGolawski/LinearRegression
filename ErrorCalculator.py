import numpy as np

class ErrorCalculator:

    def calculate_root_mean_squared_error(self, xdata, ydata, b0, b1):
        rmse = 0
        for i in range(len(xdata)):
            y_pred = b0 + b1 * xdata[i]
            rmse += (ydata[i] - y_pred) ** 2

        rmse = np.sqrt(rmse / len(xdata))
        return rmse