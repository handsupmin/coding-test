# Q061.py
# 음료수 얼려먹기

def dfs(a, b):
    if 0 <= a < len(board) and 0 <= b < len(board[0]):
        if board[a][b] == 0:
            board[a][b] = 1
            dfs(a-1, b)
            dfs(a+1, b)
            dfs(a, b-1)
            dfs(a, b+1)

n, m = map(int, input().split())
board = []
count = 0

for _ in range(n):
    board.append(list(map(int, input())))

for a in range(n):
    for b in range(m):
        if board[a][b] == 0:
            dfs(a, b)
            count += 1

print(count)

"""
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111
"""