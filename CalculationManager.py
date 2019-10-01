from math import pow as pow


class Calculator:

    def calculate_the_coefficient(self, xdata, ydata):
        x_mean = self.mean(xdata)
        y_mean = self.mean(ydata)
        numerator = 0
        denominator = 0
        for i in range(len(xdata)):
            numerator += ((xdata[i] - x_mean) * (ydata[i] - y_mean))
            denominator += pow((xdata[i] - x_mean), 2)
        return numerator / denominator

    def calculate_the_bias_coefficient(self, xdata, ydata, b1):
        return self.mean(ydata) - b1 * self.mean(xdata)

    def mean(self, data):
        return data.sum() / len(data)
