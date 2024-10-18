import sys

def determinant_4x4(matrix):
    def det3x3(m):
        return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
                - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
                + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
    
    return (matrix[0][0] * det3x3([row[1:] for row in matrix[1:]])
            - matrix[0][1] * det3x3([matrix[1]] + [[matrix[i][0]] + matrix[i][2:] for i in range(2, 4)])
            + matrix[0][2] * det3x3([matrix[1]] + [[matrix[i][0], matrix[i][1]] + [matrix[i][3]] for i in range(2, 4)])
            - matrix[0][3] * det3x3([matrix[1]] + [[matrix[i][0], matrix[i][1], matrix[i][2]] for i in range(2, 4)]))

def solve_linear_system_4x4(matrix, vector):
    det = determinant_4x4(matrix)
    if abs(det) < 1e-15:
        return None

    results = []
    for i in range(4):
        temp_matrix = [row[:] for row in matrix]
        for j in range(4):
            temp_matrix[j][i] = vector[j]
        results.append(determinant_4x4(temp_matrix) / det)

    return results

def linear_regression(X, y):
    n = len(X)
    sum_x = sum_y = sum_xy = sum_x_squared = sum_x_cubed = sum_x_to_4 = sum_x_to_6 = sum_x_to_8 = 0
    sum_yx_squared = sum_yx_cubed = 0
    
    for x, y_val in zip(X, y):
        sum_x += x
        sum_y += y_val
        sum_xy += x * y_val
        x_squared = x * x
        x_cubed = x_squared * x
        x_to_4 = x_squared * x_squared
        sum_x_squared += x_squared
        sum_x_cubed += x_cubed
        sum_x_to_4 += x_to_4
        sum_x_to_6 += x_to_4 * x_squared
        sum_x_to_8 += x_to_4 * x_to_4
        sum_yx_squared += y_val * x_squared
        sum_yx_cubed += y_val * x_cubed
    
    matrix = [
        [sum_x_to_8, sum_x_to_6, sum_x_to_4, sum_x_cubed],
        [sum_x_to_6, sum_x_to_4, sum_x_cubed, sum_x_squared],
        [sum_x_to_4, sum_x_squared, sum_x, n],
        [sum_x_cubed, sum_x_squared, sum_x, n]
    ]
    vector = [sum_yx_cubed, sum_yx_squared, sum_xy, sum_y]
    
    result = solve_linear_system_4x4(matrix, vector)
    
    return result

def main():
    X = []
    y = []
    
    for line in sys.stdin:
        x, y_val = map(float, line.split(','))
        X.append(x)
        y.append(y_val)
    
    a, b, c, d = linear_regression(X, y)
    
    output = f"{a}*x*math.pow(x, 3) + {b}*x*math.pow(x, 1) + {c}*x + {d}"
    sys.stdout.write(output + "\n")

if __name__ == "__main__":
    main()
