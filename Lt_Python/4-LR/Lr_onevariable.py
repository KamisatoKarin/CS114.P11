import numpy as np
import sys

def linear_regression(X, y):
    n = X.shape[0]
    sum_x = np.sum(X)
    sum_y = np.sum(y)
    sum_xy = np.dot(X, y)
    sum_x2 = np.dot(X, X)
    
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x)
    b = (sum_y - a * sum_x) / n
    
    return a, b

def main():
    X = []
    y = []
    for line in sys.stdin:
        line = line.strip()
        if not line:
            break
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)

    if X and y:
        X = np.array(X)
        y = np.array(y)
        a, b = linear_regression(X, y)
        print(f"{a} {b}")

if __name__ == "__main__":
    main()
