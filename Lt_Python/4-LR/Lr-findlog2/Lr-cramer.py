import sys
import math

def determinant_3x3(matrix):
    return (matrix[0][0] * (matrix[1][1] * matrix[2][2] - matrix[1][2] * matrix[2][1])
            - matrix[0][1] * (matrix[1][0] * matrix[2][2] - matrix[1][2] * matrix[2][0])
            + matrix[0][2] * (matrix[1][0] * matrix[2][1] - matrix[1][1] * matrix[2][0]))

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
            

    det = determinant_3x3(matrix)

    x = determinant_3x3([vector, matrix[1], matrix[2]]) / det
    y = determinant_3x3([matrix[0], vector, matrix[2]]) / det
    z = determinant_3x3([matrix[0], matrix[1], vector]) / det

    return x, y, z

def linear_regression(X, y):
    n = len(X)
    sum_x = sum_y = sum_xy = sum_x_squared = 0
    sum_log2x = sum_xlog2x = sum_ylog2x = sum_log2x_squared = 0
    
    for x, y_val in zip(X, y):
        log2x = math.log2(x)
        sum_x += x
        sum_y += y_val
        sum_xy += x * y_val
        sum_x_squared += x * x
        sum_log2x += log2x
        sum_xlog2x += x * log2x
        sum_ylog2x += y_val * log2x
        sum_log2x_squared += log2x * log2x
    
    matrix = [
        [sum_x_squared, sum_xlog2x, sum_x],
        [sum_xlog2x, sum_log2x_squared, sum_log2x],
        [sum_x, sum_log2x, n]
    ]
    vector = [sum_xy, sum_ylog2x, sum_y]
    
    result = solve_linear_system(matrix, vector)
    
    return result[0], result[1], result[2]

def mse(X, y, a, b, c):
    n = len(X)
    sum_squared_errors = 0
    for x, y_val in zip(X, y):
        predicted_y = a * x + b * math.log2(x) + c
        squared_error = (y_val - predicted_y) ** 2
        sum_squared_errors += squared_error
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
    
    sys.stdout.write(f"{a}*x + {b}*math.log2(x) + {c}")
    sys.stdout.write("\n")
    sys.stdout.write(f"MSE: {mse_value}")
if __name__ == "__main__":
    main()
