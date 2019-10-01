# RELATIONSHIP BETWEEN THE HEAD SIZE AND BRAIN WEIGHT
import pandas as pd
import CalculationManager as Calculator
import Visualizer as Vislzr

dataset = pd.read_csv('dataset.csv')

x_values = dataset['Head Size(cm^3)'].values
y_values = dataset['Brain Weight(grams)'].values

calculator = Calculator.Calculator()

b1 = calculator.calculate_the_coefficient(x_values, y_values)

b0 = calculator.calculate_the_bias_coefficient(x_values, y_values, b1)

print('Brain Weights = ' + str(b0) + ' + ' + str(b1) + ' * Head Size')

visualizer = Vislzr.Visualizer()

visualizer.visualize(x_values, b0, b1)