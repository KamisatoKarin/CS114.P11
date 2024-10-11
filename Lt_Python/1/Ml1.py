#chatgpt
def check_win(board):
    # Kiểm tra các hàng
    for row in board:
        if all(x == "X" for x in row):
            return True

    # Kiểm tra các cột
    for col in range(3):
        if all(board[row][col] == "X" for row in range(3)):
            return True

    # Kiểm tra đường chéo chính
    if all(board[i][i] == "X" for i in range(3)):
        return True

    # Kiểm tra đường chéo phụ
    if all(board[i][2-i] == "X" for i in range(3)):
        return True

    return False
#
board = []
for i in range(3):
    board.append(list(map(int, input().split())))

N = int(input())
numbers = [int(input()) for _ in range(N)]

for i in range(3):
    for j in range(3):
        if board[i][j] in numbers:
            board[i][j] = "X"

if check_win(board):
    print("Yes")
else:
    print("No")