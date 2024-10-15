#co su dung claude3-5 de fix TLE: su dung vong lap de tinh tong o line 
import sys

def linear_regression(X, y):
    n = len(X)
    sum_x = sum_y = sum_xy = sum_x_squared = 0
    
    for x, y_val in zip(X, y):
        sum_x += x
        sum_y += y_val
        sum_xy += x * y_val
        sum_x_squared += x * x
    
    denominator = n * sum_x_squared - sum_x * sum_x
    a = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y * sum_x_squared - sum_x * sum_xy) / denominator
    
    return a, b

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    a, b = linear_regression(X, y)
    
    sys.stdout.write(f"{a} {b}")

if __name__ == "__main__":
    main()
