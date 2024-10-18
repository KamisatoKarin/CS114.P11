import sys
import math

def determinant_4x4(matrix):
    def det3x3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))

    return (matrix[0][0] * det3x3([row[1:] for row in matrix[1:]])
            - matrix[0][1] * det3x3([row[0:1] + row[2:] for row in matrix[1:]])
            + matrix[0][2] * det3x3([row[0:2] + row[3:] for row in matrix[1:]])
            - matrix[0][3] * det3x3([row[0:3] for row in matrix[1:]]))

def solve_linear_system(matrix, vector):
    det = determinant_4x4(matrix)

    result = []
    for i in range(4):
        temp_matrix = [row[:] for row in matrix]
        for j in range(4):
            temp_matrix[j][i] = vector[j]
        result.append(determinant_4x4(temp_matrix) / det)

    return result

def linear_regression(X, y):
    n = len(X)
    sum_x = sum_y = sum_x2 = sum_x3 = sum_x4 = sum_x6 = sum_x8 = 0
    sum_xy = sum_x2y = sum_x3y = sum_x4y = 0
    
    for x, y_val in zip(X, y):
        x2 = x * x
        x3 = x2 * x
        x4 = x2 * x2
        sum_x += x
        sum_y += y_val
        sum_x2 += x2
        sum_x3 += x3
        sum_x4 += x4
        sum_x6 += x4 * x2
        sum_x8 += x4 * x4
        sum_xy += x * y_val
        sum_x2y += x2 * y_val
        sum_x3y += x3 * y_val
        sum_x4y += x4 * y_val
    
    matrix = [
        [sum_x8, sum_x6, sum_x3, sum_x4],
        [sum_x6, sum_x4, sum_x2, sum_x3],
        [sum_x3, sum_x2, sum_x, n],
        [sum_x4, sum_x3, n, sum_x2]
    ]
    vector = [sum_x4y, sum_x2y, sum_y, sum_xy]
    
    result = solve_linear_system(matrix, vector)
    
    if result is None:
        return 0, 0, 0, sum_y / n
    
    return result

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    result = linear_regression(X, y)
    
    a, b, c, d = result
    sys.stdout.write(f"{a}*math.pow(x,4) + {b}*math.pow(x,2) + {c}*x + {d}")

if __name__ == "__main__":
    main()
