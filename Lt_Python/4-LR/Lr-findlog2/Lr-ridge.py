import sys
import math
import numpy as np

def ridge_regression(X, y, alpha=0.1):
    m = len(y)
    X = np.column_stack((X, np.log2(X), np.ones(m)))
    n = X.shape[1]
    
    I = np.eye(n)
    I[n-1, n-1] = 0  # Don't regularize the bias term
    
    theta = np.linalg.inv(X.T.dot(X) + alpha * I).dot(X.T).dot(y)
    return theta

def linear_regression(X, y):
    X = np.array(X)
    y = np.array(y)
    theta = ridge_regression(X, y)
    return theta[0], theta[1], theta[2]

def mse(X, y, a, b, c):
    n = len(X)
    sum_squared_errors = sum((y[i] - (a * X[i] + b * math.log2(X[i]) + c))**2 for i in range(n))
    return sum_squared_errors / n

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    a, b, c = linear_regression(X, y)
    mse_value = mse(X, y, a, b, c)
    
    sys.stdout.write(f"{a}*x + {b}*math.log2(x) + {c}\n")
    sys.stdout.write(f"MSE: {mse_value}\n")

if __name__ == "__main__":
    main()
