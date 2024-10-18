import sys
import math

def determinant_4x4(matrix):
    return (matrix[0][0] * (matrix[1][1] * (matrix[2][2] * matrix[3][3] - matrix[2][3] * matrix[3][2]) -
                            matrix[1][2] * (matrix[2][1] * matrix[3][3] - matrix[2][3] * matrix[3][1]) +
                            matrix[1][3] * (matrix[2][1] * matrix[3][2] - matrix[2][2] * matrix[3][1])) -
            matrix[0][1] * (matrix[1][0] * (matrix[2][2] * matrix[3][3] - matrix[2][3] * matrix[3][2]) -
                            matrix[1][2] * (matrix[2][0] * matrix[3][3] - matrix[2][3] * matrix[3][0]) +
                            matrix[1][3] * (matrix[2][0] * matrix[3][2] - matrix[2][2] * matrix[3][0])) +
            matrix[0][2] * (matrix[1][0] * (matrix[2][1] * matrix[3][3] - matrix[2][3] * matrix[3][1]) -
                            matrix[1][1] * (matrix[2][0] * matrix[3][3] - matrix[2][3] * matrix[3][0]) +
                            matrix[1][3] * (matrix[2][0] * matrix[3][1] - matrix[2][1] * matrix[3][0])) -
            matrix[0][3] * (matrix[1][0] * (matrix[2][1] * matrix[3][2] - matrix[2][2] * matrix[3][1]) -
                            matrix[1][1] * (matrix[2][0] * matrix[3][2] - matrix[2][2] * matrix[3][0]) +
                            matrix[1][2] * (matrix[2][0] * matrix[3][1] - matrix[2][1] * matrix[3][0])))

def solve_linear_system(matrix, vector):
    n = len(matrix)
    for i in range(n):
        max_element = abs(matrix[i][i])
        max_row = i  
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_element:
                max_element = abs(matrix[k][i])
                max_row = k

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        vector[i], vector[max_row] = vector[max_row], vector[i]
            
    det = determinant_4x4(matrix)

    x = determinant_4x4([vector, matrix[1], matrix[2], matrix[3]]) / det
    y = determinant_4x4([matrix[0], vector, matrix[2], matrix[3]]) / det
    z = determinant_4x4([matrix[0], matrix[1], vector, matrix[3]]) / det
    w = determinant_4x4([matrix[0], matrix[1], matrix[2], vector]) / det

    return x, y, z, w

def linear_regression(X, y):
    n = len(X)
    sum_x = sum_x2 = sum_x3 = sum_x4 = sum_x5 = sum_x6 = sum_x7 = sum_x8 = 0
    sum_y = sum_xy = sum_x2y = sum_x4y = 0
    
    for x, y_val in zip(X, y):
        sum_x += x
        sum_x2 += x**2
        sum_x3 += x**3
        sum_x4 += x**4
        sum_x5 += x**5
        sum_x6 += x**6
        sum_x7 += x**7
        sum_x8 += x**8
        sum_y += y_val
        sum_xy += x * y_val
        sum_x2y += x**2 * y_val
        sum_x4y += x**4 * y_val
    
    matrix = [
        [sum_x8, sum_x6, sum_x5, sum_x4],
        [sum_x6, sum_x4, sum_x3, sum_x2],
        [sum_x5, sum_x3, sum_x2, sum_x],
        [sum_x4, sum_x2, sum_x, n]
    ]
    vector = [sum_x4y, sum_x2y, sum_xy, sum_y]
    
    result = solve_linear_system(matrix, vector)
    
    return result[0], result[1], result[2], result[3]

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
