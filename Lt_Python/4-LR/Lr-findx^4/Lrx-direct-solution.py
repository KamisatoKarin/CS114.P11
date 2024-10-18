import sys
import math

def matrix_multiply(A, B):
    return [[sum(a*b for a,b in zip(A_row,B_col)) for B_col in zip(*B)] for A_row in A]

def transpose(A):
    return list(map(list, zip(*A)))

def matrix_vector_multiply(A, v):
    return [sum(a*b for a,b in zip(row, v)) for row in A]

def dot_product(v1, v2):
    return sum(a*b for a,b in zip(v1, v2))

def linear_regression(X, y):
    # Tạo ma trận thiết kế
    A = [[x**4, x**2, x, 1] for x in X]
    AT = transpose(A)
    
    # Tính ATA và ATy
    ATA = matrix_multiply(AT, A)
    ATy = matrix_vector_multiply(AT, y)
    
    # Giải hệ phương trình tuyến tính bằng phương pháp Cramer
    det = (ATA[0][0] * (ATA[1][1] * (ATA[2][2] * ATA[3][3] - ATA[2][3] * ATA[3][2]) - 
                        ATA[1][2] * (ATA[2][1] * ATA[3][3] - ATA[2][3] * ATA[3][1]) +
                        ATA[1][3] * (ATA[2][1] * ATA[3][2] - ATA[2][2] * ATA[3][1])) -
           ATA[0][1] * (ATA[1][0] * (ATA[2][2] * ATA[3][3] - ATA[2][3] * ATA[3][2]) -
                        ATA[1][2] * (ATA[2][0] * ATA[3][3] - ATA[2][3] * ATA[3][0]) +
                        ATA[1][3] * (ATA[2][0] * ATA[3][2] - ATA[2][2] * ATA[3][0])) +
           ATA[0][2] * (ATA[1][0] * (ATA[2][1] * ATA[3][3] - ATA[2][3] * ATA[3][1]) -
                        ATA[1][1] * (ATA[2][0] * ATA[3][3] - ATA[2][3] * ATA[3][0]) +
                        ATA[1][3] * (ATA[2][0] * ATA[3][1] - ATA[2][1] * ATA[3][0])) -
           ATA[0][3] * (ATA[1][0] * (ATA[2][1] * ATA[3][2] - ATA[2][2] * ATA[3][1]) -
                        ATA[1][1] * (ATA[2][0] * ATA[3][2] - ATA[2][2] * ATA[3][0]) +
                        ATA[1][2] * (ATA[2][0] * ATA[3][1] - ATA[2][1] * ATA[3][0])))

    # Tính các định thức cho a, b, c, d
    det_a = (ATy[0] * (ATA[1][1] * (ATA[2][2] * ATA[3][3] - ATA[2][3] * ATA[3][2]) - 
                       ATA[1][2] * (ATA[2][1] * ATA[3][3] - ATA[2][3] * ATA[3][1]) +
                       ATA[1][3] * (ATA[2][1] * ATA[3][2] - ATA[2][2] * ATA[3][1])) -
             ATA[0][1] * (ATy[1] * (ATA[2][2] * ATA[3][3] - ATA[2][3] * ATA[3][2]) -
                          ATA[1][2] * (ATy[2] * ATA[3][3] - ATA[2][3] * ATy[3]) +
                          ATA[1][3] * (ATy[2] * ATA[3][2] - ATA[2][2] * ATy[3])) +
             ATA[0][2] * (ATy[1] * (ATA[2][1] * ATA[3][3] - ATA[2][3] * ATA[3][1]) -
                          ATA[1][1] * (ATy[2] * ATA[3][3] - ATA[2][3] * ATy[3]) +
                          ATA[1][3] * (ATy[2] * ATA[3][1] - ATA[2][1] * ATy[3])) -
             ATA[0][3] * (ATy[1] * (ATA[2][1] * ATA[3][2] - ATA[2][2] * ATA[3][1]) -
                          ATA[1][1] * (ATy[2] * ATA[3][2] - ATA[2][2] * ATy[3]) +
                          ATA[1][2] * (ATy[2] * ATA[3][1] - ATA[2][1] * ATy[3])))

    det_b = (ATA[0][0] * (ATy[1] * (ATA[2][2] * ATA[3][3] - ATA[2][3] * ATA[3][2]) -
                          ATA[1][2] * (ATy[2] * ATA[3][3] - ATA[2][3] * ATy[3]) +
                          ATA[1][3] * (ATy[2] * ATA[3][2] - ATA[2][2] * ATy[3])) -
             ATy[0] * (ATA[1][0] * (ATA[2][2] * ATA[3][3] - ATA[2][3] * ATA[3][2]) -
                       ATA[1][2] * (ATA[2][0] * ATA[3][3] - ATA[2][3] * ATA[3][0]) +
                       ATA[1][3] * (ATA[2][0] * ATA[3][2] - ATA[2][2] * ATA[3][0])) +
             ATA[0][2] * (ATA[1][0] * (ATy[2] * ATA[3][3] - ATA[2][3] * ATy[3]) -
                          ATy[1] * (ATA[2][0] * ATA[3][3] - ATA[2][3] * ATA[3][0]) +
                          ATA[1][3] * (ATA[2][0] * ATy[3] - ATy[2] * ATA[3][0])) -
             ATA[0][3] * (ATA[1][0] * (ATy[2] * ATA[3][2] - ATA[2][2] * ATy[3]) -
                          ATy[1] * (ATA[2][0] * ATA[3][2] - ATA[2][2] * ATA[3][0]) +
                          ATA[1][2] * (ATA[2][0] * ATy[3] - ATy[2] * ATA[3][0])))

    det_c = (ATA[0][0] * (ATA[1][1] * (ATy[2] * ATA[3][3] - ATA[2][3] * ATy[3]) -
                          ATy[1] * (ATA[2][1] * ATA[3][3] - ATA[2][3] * ATA[3][1]) +
                          ATA[1][3] * (ATA[2][1] * ATy[3] - ATy[2] * ATA[3][1])) -
             ATA[0][1] * (ATA[1][0] * (ATy[2] * ATA[3][3] - ATA[2][3] * ATy[3]) -
                          ATy[1] * (ATA[2][0] * ATA[3][3] - ATA[2][3] * ATA[3][0]) +
                          ATA[1][3] * (ATA[2][0] * ATy[3] - ATy[2] * ATA[3][0])) +
             ATy[0] * (ATA[1][0] * (ATA[2][1] * ATA[3][3] - ATA[2][3] * ATA[3][1]) -
                       ATA[1][1] * (ATA[2][0] * ATA[3][3] - ATA[2][3] * ATA[3][0]) +
                       ATA[1][3] * (ATA[2][0] * ATA[3][1] - ATA[2][1] * ATA[3][0])) -
             ATA[0][3] * (ATA[1][0] * (ATA[2][1] * ATy[3] - ATy[2] * ATA[3][1]) -
                          ATA[1][1] * (ATA[2][0] * ATy[3] - ATy[2] * ATA[3][0]) +
                          ATy[1] * (ATA[2][0] * ATA[3][1] - ATA[2][1] * ATA[3][0])))

    det_d = (ATA[0][0] * (ATA[1][1] * (ATA[2][2] * ATy[3] - ATy[2] * ATA[3][2]) -
                          ATA[1][2] * (ATA[2][1] * ATy[3] - ATy[2] * ATA[3][1]) +
                          ATy[1] * (ATA[2][1] * ATA[3][2] - ATA[2][2] * ATA[3][1])) -
             ATA[0][1] * (ATA[1][0] * (ATA[2][2] * ATy[3] - ATy[2] * ATA[3][2]) -
                          ATA[1][2] * (ATA[2][0] * ATy[3] - ATy[2] * ATA[3][0]) +
                          ATy[1] * (ATA[2][0] * ATA[3][2] - ATA[2][2] * ATA[3][0])) +
             ATA[0][2] * (ATA[1][0] * (ATA[2][1] * ATy[3] - ATy[2] * ATA[3][1]) -
                          ATA[1][1] * (ATA[2][0] * ATy[3] - ATy[2] * ATA[3][0]) +
                          ATy[1] * (ATA[2][0] * ATA[3][1] - ATA[2][1] * ATA[3][0])) -
             ATy[0] * (ATA[1][0] * (ATA[2][1] * ATA[3][2] - ATA[2][2] * ATA[3][1]) -
                       ATA[1][1] * (ATA[2][0] * ATA[3][2] - ATA[2][2] * ATA[3][0]) +
                       ATA[1][2] * (ATA[2][0] * ATA[3][1] - ATA[2][1] * ATA[3][0])))
    
    a = det_a / det
    b = det_b / det
    c = det_c / det
    d = det_d / det
    
    return a, b, c, d

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
    
    output = f"{a}*x*math.pow(x, 3) + {b}*x*math.pow(x, 1) + {c}*x + {d}"
    sys.stdout.write(output + "\n")
    sys.stdout.write(f"MSE: {mse_value}\n")

if __name__ == "__main__":
    main()
