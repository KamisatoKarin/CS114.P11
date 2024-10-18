import sys
import math

def dot_product(v1, v2):
    return sum(x*y for x,y in zip(v1, v2))

def matrix_vector_multiply(A, x):
    return [dot_product(row, x) for row in A]

def vector_subtract(v1, v2):
    return [x-y for x,y in zip(v1, v2)]

def conjugate_gradient_method(A, b, max_iterations=1000, tolerance=1e-10):
    n = len(A)
    x = [0] * n
    r = b.copy()
    p = r.copy()
    
    for _ in range(max_iterations):
        Ap = matrix_vector_multiply(A, p)
        alpha = dot_product(r, r) / dot_product(p, Ap)
        
        x_new = [x[i] + alpha * p[i] for i in range(n)]
        r_new = vector_subtract(r, [alpha * Ap_i for Ap_i in Ap])
        
        if math.sqrt(dot_product(r_new, r_new)) < tolerance:
            return x_new
        
        beta = dot_product(r_new, r_new) / dot_product(r, r)
        p = [r_new[i] + beta * p[i] for i in range(n)]
        
        x = x_new
        r = r_new
    
    return x

def linear_regression(X, y):
    n = len(X)
    X_design = [[x**2, x*math.log2(x), x, x*math.log2(x), math.log2(x)**2, math.log2(x), x, math.log2(x), 1] for x in X]
    
    A = [[sum(row[i] * row[j] for row in X_design) for j in range(3)] for i in range(3)]
    b = [sum(row[i] * y[j] for j, row in enumerate(X_design)) for i in range(3)]
    
    beta = conjugate_gradient_method(A, b)
    
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
