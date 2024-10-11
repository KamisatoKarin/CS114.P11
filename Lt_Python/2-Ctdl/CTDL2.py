def read_input():
    matrix = []
    for _ in range(4):
        row = list(map(int, input().split()))
        if len(row) != 4:  
            raise ValueError()
        matrix.append(row)
    
    direction = input().strip()
    if direction not in ('L', 'R', 'U', 'D'):  
        raise ValueError()
    return matrix, direction

def slide_left(matrix):
    new_matrix = []
    for row in matrix:
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1):
            if new_row[i] == new_row[i + 1]:
                new_row[i] *= 2
                new_row[i + 1] = 0
        new_row = [num for num in new_row if num != 0]
        new_row += [0] * (4 - len(new_row))
        new_matrix.append(new_row)
    return new_matrix

def slide_right(matrix):
    new_matrix = []
    for row in matrix:
        new_row = [num for num in row if num != 0]
        for i in range(len(new_row) - 1, 0, -1):
            if new_row[i] == new_row[i - 1]:
                new_row[i] *= 2
                new_row[i - 1] = 0
        new_row = [num for num in new_row if num != 0]
        new_row = [0] * (4 - len(new_row)) + new_row
        new_matrix.append(new_row)
    return new_matrix

def slide_up(matrix):
    transposed = list(zip(*matrix))
    transposed = slide_left(transposed)
    return [list(row) for row in zip(*transposed)]

def slide_down(matrix):
    transposed = list(zip(*matrix))
    transposed = slide_right(transposed)
    return [list(row) for row in zip(*transposed)]

def slide(matrix, direction):
    if direction == 'L':
        return slide_left(matrix)
    elif direction == 'R':
        return slide_right(matrix)
    elif direction == 'U':
        return slide_up(matrix)
    elif direction == 'D':
        return slide_down(matrix)
    else:
        raise ValueError("Invalid direction")

matrix, direction = read_input()
new_matrix = slide(matrix, direction)

for row in new_matrix:
    print(" ".join(map(str, row)))
