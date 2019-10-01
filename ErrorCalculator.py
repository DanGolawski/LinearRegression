import numpy as np

class ErrorCalculator:

    def calculate_root_mean_squared_error(self, xdata, ydata, b0, b1):
        rmse = 0
        for i in range(len(xdata)):
            y_pred = b0 + b1 * xdata[i]
            rmse += (ydata[i] - y_pred) ** 2

        rmse = np.sqrt(rmse / len(xdata))
        return rmse

    def calculate_R_squared(self, xdata, ydata, b0, b1):
        sumofsquares = 0
        sumofresiduals = 0
        y_mean = np.mean(ydata)
        for i in range(len(xdata)):
            y_pred = b0 + b1 * xdata[i]
            sumofsquares += (ydata[i] - y_mean) ** 2
            sumofresiduals += (ydata[i] - y_pred) ** 2

        score = 1 - (sumofresiduals / sumofsquares)
        return score