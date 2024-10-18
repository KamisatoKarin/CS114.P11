import sys
import math

def dot_product(v1, v2):
    return sum(x*y for x,y in zip(v1, v2))

def scalar_multiply(s, v):
    return [s*x for x in v]

def vector_subtract(v1, v2):
    return [x-y for x,y in zip(v1, v2)]

def gram_schmidt(A):
    Q = []
    for a in A:
        q = a
        for u in Q:
            q = vector_subtract(q, scalar_multiply(dot_product(u, a) / dot_product(u, u), u))
        Q.append(scalar_multiply(1/math.sqrt(dot_product(q, q)), q))
    return Q

def qr_decomposition(A):
    Q = gram_schmidt(transpose(A))
    Q = transpose(Q)
    R = [[dot_product(Q[i], A[j]) for j in range(len(A[0]))] for i in range(len(A))]
    return Q, R

def transpose(A):
    return list(map(list, zip(*A)))

def back_substitution(R, b):
    n = len(R)
    x = [0] * n
    for i in range(n-1, -1, -1):
        x[i] = b[i]
        for j in range(i+1, n):
            x[i] -= R[i][j] * x[j]
        x[i] /= R[i][i]
    return x

def linear_regression(X, y):
    n = len(X)
    X_design = [[x, math.log2(x), 1] for x in X]
    
    Q, R = qr_decomposition(X_design)
    Q_transpose = transpose(Q)
    b = [dot_product(Q_transpose[i], y) for i in range(len(Q_transpose))]
    
    beta = back_substitution(R, b)
    
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
