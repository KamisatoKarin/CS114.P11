import sys
import math

def custom_regression(X, y):
    n = len(X)
    sum_x = sum_y = sum_xy = sum_sin_x = sum_y_sin_x = 0
    
    for x, y_val in zip(X, y):
        sin_x = math.sin(x)
        sum_x += x
        sum_y += y_val
        sum_xy += x * y_val
        sum_sin_x += sin_x
        sum_y_sin_x += y_val * sin_x
    
    denominator = n * sum_x * sum_sin_x - sum_x * sum_x * sum_sin_x
    a = (n * sum_xy * sum_sin_x - sum_x * sum_y * sum_sin_x) / denominator
    b = (n * sum_x * sum_y_sin_x - sum_x * sum_y * sum_x) / denominator
    
    mean_y = sum_y / n
    mean_x = sum_x / n
    mean_sin_x = sum_sin_x / n
    
    c = mean_y - a * mean_x - b * mean_sin_x
    
    return a, b, c

def calculate_mse(X, y, a, b, c):
    mse = 0
    n = len(X)
    for x, y_actual in zip(X, y):
        y_predicted = a * x + b * math.sin(x) + c
        mse += (y_actual - y_predicted) ** 2
    return mse / n

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    a, b, c = custom_regression(X, y)
    
    equation = f"{a}*x + {b}*math.sin(x) + {c}"
    a1= 2.1355915331251682e-07
    b1= -2.210278535318776
    c1= 51.07807590082174
    mse = calculate_mse(X, y, a, b, c)
    mse1 = calculate_mse(X, y, a1, b1, c1)
    
    sys.stdout.write(f"{equation}\n")
    sys.stdout.write(f"MSE: {mse}\n")
    sys.stdout.write(f"MSE goc: {mse1}")

if __name__ == "__main__":
    main()
