import numpy as np
import sys

def linear_regression(X, y):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(y)
    sum_xy = np.sum(X * y)
    sum_x2 = np.sum(X * X)
    
    denominator = n * sum_x2 - sum_x * sum_x
    
    a = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y - a * sum_x) / n
    
    return a, b

def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    
    data = np.genfromtxt(input_data.splitlines(), delimiter=',')
    X = data[:, 0]
    y = data[:, 1]
    
    a, b = linear_regression(X, y)
    
    print(a, b)

if __name__ == "__main__":
    main()