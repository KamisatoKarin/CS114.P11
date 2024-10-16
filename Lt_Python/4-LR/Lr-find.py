import numpy as np
from scipy.optimize import curve_fit
import math
import sys

def model(x, a, b, c):
    return a * x + b * np.log2(x) + c

def linear_regression_with_log():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    X = np.array(X)
    y = np.array(y)
    
    popt, _ = curve_fit(model, X, y)
    
    equation = f"{popt[0]} * x + {popt[1]} * math.log2(x) + {popt[2]}"
    return equation

def main():
    equation = linear_regression_with_log()
    sys.stdout.write(equation)

if __name__ == "__main__":
    main()
