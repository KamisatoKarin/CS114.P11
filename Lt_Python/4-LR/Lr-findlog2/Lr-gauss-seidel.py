import sys
import math

def gauss_seidel_method(A, b, max_iterations=1000, tolerance=1e-10):
    n = len(A)
    x = [0] * n
    
    for _ in range(max_iterations):
        x_new = x.copy()
        for i in range(n):
            s1 = sum(A[i][j] * x_new[j] for j in range(i))
            s2 = sum(A[i][j] * x[j] for j in range(i + 1, n))
            x_new[i] = (b[i] - s1 - s2) / A[i][i]
        
        if max(abs(x_new[i] - x[i]) for i in range(n)) < tolerance:
            return x_new
        x = x_new
    
    return x

def linear_regression(X, y):
    n = len(X)
    X_design = [[x**2, x*math.log2(x), x, x*math.log2(x), math.log2(x)**2, math.log2(x), x, math.log2(x), 1] for x in X]
    
    A = [[sum(row[i] * row[j] for row in X_design) for j in range(3)] for i in range(3)]
    b = [sum(row[i] * y[j] for j, row in enumerate(X_design)) for i in range(3)]
    
    beta = gauss_seidel_method(A, b)
    
    return beta[0], beta[1], beta[2]

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
