import sys
import math

def cholesky_decomposition(A):
    n = len(A)
    L = [[0.0] * n for i in range(n)]

    for i in range(n):
        for j in range(i+1):
            sum_k = sum(L[i][k] * L[j][k] for k in range(j))
            
            if i == j:
                L[i][j] = math.sqrt(A[i][i] - sum_k)
            else:
                L[i][j] = (A[i][j] - sum_k) / L[j][j]
                
    return L

def forward_substitution(L, b):
    n = len(L)
    y = [0] * n
    for i in range(n):
        y[i] = (b[i] - sum(L[i][j] * y[j] for j in range(i))) / L[i][i]
    return y

def backward_substitution(LT, y):
    n = len(LT)
    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - sum(LT[j][i] * x[j] for j in range(i + 1, n))) / LT[i][i]
    return x

def linear_regression(X, y):
    n = len(X)
    X_design = [[x, math.log2(x), 1] for x in X]
    
    XTX = [[sum(row[i] * row[j] for row in X_design) for j in range(3)] for i in range(3)]
    XTy = [sum(X_design[i][j] * y[i] for i in range(n)) for j in range(3)]
    
    L = cholesky_decomposition(XTX)
    LT = list(map(list, zip(*L)))  # Transpose of L
    
    y = forward_substitution(L, XTy)
    beta = backward_substitution(LT, y)
    
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
