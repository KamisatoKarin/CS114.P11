import sys
import math

def matrix_multiply(A, B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]

def transpose(A):
    return list(map(list, zip(*A)))

def minor(A, i, j):
    return [row[:j] + row[j+1:] for row in (A[:i] + A[i+1:])]

def determinant(A):
    if len(A) == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]
    det = 0
    for j in range(len(A)):
        det += ((-1)**j) * A[0][j] * determinant(minor(A, 0, j))
    return det

def inverse(A):
    det = determinant(A)
    if len(A) == 2:
        return [[A[1][1]/det, -1*A[0][1]/det],
                [-1*A[1][0]/det, A[0][0]/det]]
    cofactors = []
    for r in range(len(A)):
        cofactorRow = []
        for c in range(len(A)):
            minor_det = determinant(minor(A, r, c))
            cofactorRow.append(((-1)**(r+c)) * minor_det)
        cofactors.append(cofactorRow)
    cofactors = transpose(cofactors)
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c] / det
    return cofactors

def linear_regression(X, y):
    n = len(X)
    X_design = [[x, math.log2(x), 1] for x in X]
    X_transpose = transpose(X_design)
    
    XTX = matrix_multiply(X_transpose, X_design)
    XTy = matrix_multiply(X_transpose, [[yi] for yi in y])
    
    XTX_inv = inverse(XTX)
    beta = matrix_multiply(XTX_inv, XTy)
    
    return beta[0][0], beta[1][0], beta[2][0]

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
