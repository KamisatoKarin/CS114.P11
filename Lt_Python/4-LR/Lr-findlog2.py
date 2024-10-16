import sys
import math

def calculate_mse(X, y, a, b, c):
    mse = 0
    n = len(X)
    for x, y_actual in zip(X, y):
        y_predicted = a * x + b * math.log2(x) + c
        mse += (y_actual - y_predicted) ** 2
    return mse / n

def linear_regression(X, y):
    n = len(X)
    sum_x = sum_y = sum_xy = sum_x_squared = 0
    sum_log_x = sum_y_log_x = sum_log_x_squared = 0
    
    for x, y_val in zip(X, y):
        log_x = math.log2(x)
        sum_x += x
        sum_y += y_val
        sum_xy += x * y_val
        sum_x_squared += x * x
        sum_log_x += log_x
        sum_y_log_x += y_val * log_x
        sum_log_x_squared += log_x * log_x
    
    denominator = n * sum_x_squared - sum_x * sum_x
    a = (n * sum_xy - sum_x * sum_y) / denominator
    
    denominator_log = n * sum_log_x_squared - sum_log_x * sum_log_x
    b = (n * sum_y_log_x - sum_y * sum_log_x) / denominator_log
    
    return a, b

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    a, b = linear_regression(X, y)
    
    mean_x = sum(X) / len(X)
    mean_y = sum(y) / len(y)
    mean_log_x = sum(math.log2(x) for x in X) / len(X)
    
    c = mean_y - a * mean_x - b * mean_log_x

    mse = calculate_mse(X, y, a, b, c)

    a1= 2.1355915331251682e-07
    b1= -2.210278535318776
    c1= 51.07807590082174

    mse1 = calculate_mse(X, y, a1, b1, c1)

    equation = f"{a:.16e}*x + {b:.15f}*math.log2(x) + {c:.14f}"
    sys.stdout.write(equation)
    sys.stderr.write(f"\nMse1: {mse1}")
    sys.stderr.write(f"\nMse: {mse}")

if __name__ == "__main__":
    main()
