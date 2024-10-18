import sys
import math

def linear_regression(X, y):
    n = len(X)
    sum_x = sum_y = sum_xy = sum_x_squared = 0
    
    for x, y_val in zip(X, y):
        sum_x += x
        sum_y += y_val
        sum_xy += x * y_val
        sum_x_squared += x * x
    
    denominator = n * sum_x_squared - sum_x * sum_x
    if denominator == 0:
        return 0, sum_y / n  
    a = (n * sum_xy - sum_x * sum_y) / denominator
    b = (sum_y * sum_x_squared - sum_x * sum_xy) / denominator
    
    return a, b

def calculate_mse(X, y, func):
    return sum((func(x) - y_val) ** 2 for x, y_val in zip(X, y)) / len(X)

def find_best_function(X, y):
    functions = [
        ("linear", lambda a, b: lambda x: a*x + b, lambda x: x),
        ("quadratic", lambda a, b, c: lambda x: a*x**2 + b*x + c, lambda x: x**2),
        ("cubic", lambda a, b, c, d: lambda x: a*x**3 + b*x**2 + c*x + d, lambda x: x**3),
        ("log", lambda a, b: lambda x: a*math.log(max(x, 1e-10)) + b, lambda x: math.log(max(x, 1e-10))),
        ("exp", lambda a, b: lambda x: a*math.exp(min(x, 100)) + b, lambda x: math.exp(min(x, 100))),
        ("sin", lambda a, b: lambda x: a*math.sin(x) + b, lambda x: math.sin(x)),
    ]

    best_func = None
    best_mse = float('inf')
    best_params = None
    best_name = None

    for name, func_template, transform in functions:
        try:
            X_transformed = [transform(x) for x in X]
            params = linear_regression(X_transformed, y)
            
            if name == "quadratic":
                a, b = params
                c = sum(y) / len(y) - a * sum(x**2 for x in X) / len(X) - b * sum(X) / len(X)
                params = (a, b, c)
            elif name == "cubic":
                a, b = params
                c = sum(y) / len(y) - a * sum(x**3 for x in X) / len(X) - b * sum(x**2 for x in X) / len(X)
                d = sum(y) / len(y) - a * sum(x**3 for x in X) / len(X) - b * sum(x**2 for x in X) / len(X) - c * sum(X) / len(X)
                params = (a, b, c, d)
            
            func = func_template(*params)
            mse = calculate_mse(X, y, func)
            
            if mse < best_mse:
                best_mse = mse
                best_func = func
                best_params = params
                best_name = name
        except Exception as e:
            print(f"Error with {name} function: {e}")
            continue

    return best_name, best_func, best_params, best_mse

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        try:
            x, y_val = map(float, line.strip().split(','))
            X.append(x)
            y.append(y_val)
        except ValueError:
            print(f"Skipping invalid line: {line}")
    
    if not X or not y:
        print("No valid data points found.")
        return

    func_name, func, params, mse = find_best_function(X, y)
    
    if func_name == "linear":
        a, b = params
        equation = f"{a}*x + {b}"
    elif func_name == "quadratic":
        a, b, c = params
        equation = f"{a}*x**2 + {b}*x + {c}"
    elif func_name == "cubic":
        a, b, c, d = params
        equation = f"{a}*x**3 + {b}*x**2 + {c}*x + {d}"
    elif func_name == "log":
        a, b = params
        equation = f"{a}*math.log(max(x, 1e-10)) + {b}"
    elif func_name == "exp":
        a, b = params
        equation = f"{a}*math.exp(min(x, 100)) + {b}"
    elif func_name == "sin":
        a, b = params
        equation = f"{a}*math.sin(x) + {b}"
    else:
        print("No suitable function found.")
        return
    
    print(f"y = {equation}")
    print(f"MSE: {mse}")

if __name__ == "__main__":
    main()
