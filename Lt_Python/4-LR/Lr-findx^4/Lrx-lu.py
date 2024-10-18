import sys
import math

def lu_decomposition(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]
    U = [[0.0] * n for i in range(n)]

    for i in range(n):
        L[i][i] = 1.0
        for j in range(i, n):
            U[i][j] = A[i][j] - sum(L[i][k] * U[k][j] for k in range(i))
        for j in range(i + 1, n):
            L[j][i] = (A[j][i] - sum(L[j][k] * U[k][i] for k in range(i))) / U[i][i]

    return L, U

def forward_substitution(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        y[i] = b[i] - sum(L[i][j] * y[j] for j in range(i))
    return y

def backward_substitution(U, y):
    n = len(U)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(U[i][j] * x[j] for j in range(i + 1, n))) / U[i][i]
    return x

def linear_regression(X, y):
    n = len(X)
    X_design = [[x**4, x**2, x, 1] for x in X]
    
    XTX = [[sum(row[i] * row[j] for row in X_design) for j in range(4)] for i in range(4)]
    XTy = [sum(X_design[i][j] * y[i] for i in range(n)) for j in range(4)]
    
    L, U = lu_decomposition(XTX)
    y = forward_substitution(L, XTy)
    beta = backward_substitution(U, y)
    
    return beta[0], beta[1], beta[2], beta[3]

def mse(X, y, a, b, c, d):
    n = len(X)
    sum_squared_errors = sum((y[i] - (a * X[i]**4 + b * X[i]**2 + c * X[i] + d))**2 for i in range(n))
    return sum_squared_errors / n

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    a, b, c, d = linear_regression(X, y)
    mse_value = mse(X, y, a, b, c, d)
    
    sys.stdout.write(f"{a}*x*math.pow(x,3) + {b}*x*math.pow(x,1) + {c}*x + {d}\n")
    sys.stdout.write(f"MSE: {mse_value}\n")

if __name__ == "__main__":
    main()
