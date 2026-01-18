import numpy as np

def fit_linear_model(prices):
    x = np.arange(len(prices))
    coeffs = np.polyfit(x, prices.values, 1)
    return coeffs

def predict(coeffs, length):
    x = np.arange(length)
    return coeffs[0] * x + coeffs[1]
