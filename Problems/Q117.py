# Q117.py
# https://www.acmicpc.net/problem/1018

m, n = map(int, input().split())

chess_board = []
for _ in range(m):
    chess_board.append(list(map(str, input())))

white_row = ['W', 'B'] * 4

white_board = []
black_board = []

for i in range(8):
    white_board.append(white_row)
    white_row = white_row[::-1]
    black_board.append(white_row)

result = []

for i in range(m - 7):
    for j in range(n - 7):
        w_result = 0
        b_result = 0
        for a in range(8):
            for b in range(8):
                if chess_board[i + a][j + b] != white_board[a][b]:
                    w_result += 1
                if chess_board[i + a][j + b] != black_board[a][b]:
                    b_result += 1
        result.append(min(w_result, b_result))

print(min(result))
