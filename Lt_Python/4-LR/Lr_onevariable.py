import numpy as np
import pandas as pd
import sys
import io

def linear_regression(X, y):
    n = len(X)
    sum_x = np.sum(X)
    sum_y = np.sum(y)
    sum_xy = np.sum(X * y)
    sum_x2 = np.sum(X * X)
    
    a = (n * sum_xy - sum_x * sum_y) / (n * sum_x2 - sum_x * sum_x )
    b = (sum_y - a * sum_x) / n
    
    return a, b

def main():
    input_data = sys.stdin.read().strip()
    if not input_data:
        return
    data = pd.read_csv(io.StringIO(input_data), header=None)
    X = data[0].values
    y = data[1].values
    
    a, b = linear_regression(X, y)
    
    print(a, b)

if __name__ == "__main__":
    main()
