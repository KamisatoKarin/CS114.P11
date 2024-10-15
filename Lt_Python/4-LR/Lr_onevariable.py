import numpy as np
import sys

def linear_regression(X, y):
    n = len(X)
    X_mean = np.mean(X)
    y_mean = np.mean(y)
    
    SS_xy = np.dot(X - X_mean, y - y_mean)
    SS_xx = np.dot(X - X_mean, X - X_mean)
    
    a = SS_xy / SS_xx
    b = y_mean - a * X_mean
    
    return a, b

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        if line.strip():
            x, y_val = map(float, line.strip().split(','))
            X.append(x)
            y.append(y_val)
    
    if not X or not y:
        return
    
    X = np.array(X)
    y = np.array(y)
    
    a, b = linear_regression(X, y)
    
    print(f"{a} {b}")

if __name__ == "__main__":
    main()
