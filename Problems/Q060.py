# Q060.py
# https://programmers.co.kr/learn/courses/30/lessons/60063?language=python3

from collections import deque

INF = int(1e9)

def bfs(board):
    q = deque
    n = len(board)
    move = [[(-2,0),(-1,0)], [(0,-2),(0,-1)], [(2,0),(1,0)], [(0,2),(0,1)]]
    wall = [(-1,-1), (1,-1), (1,1), (-1,1)]
    rotate = [(-1,0), (0,-1), (1,0), (0,1), (-1,0)]
    
    for i in range(n):
        for j in range(n):
            if board[i][j] == INF:
                isMove = False
                for t in move:
                    x1 = i + t[0][0]
                    x2 = i + t[1][0]
                    y1 = j + t[0][1]
                    y2 = j + t[1][1]
                    if 0 <= x1 < n and 0 <= x2 < n and 0 <= y1 < n and 0 <= y2 < n and board[x1][y1] != -1 and board[x1][y1] != INF and board[x2][y2] != -1 and board[x2][y2] != INF:
                        board[i][j] = max(board[x1][y1], board[x2][y2])+1
                        isMove = True
                if not isMove:
                    for w in range(4):
                        wx = i + wall[w][0]
                        wy = j + wall[w][1]                    
                        x1 = i + rotate[w][0]
                        x2 = i + rotate[w+1][0]
                        y1 = j + rotate[w][1]
                        y2 = j + rotate[w+1][1]
                        if 0 <= wx < n and 0 <= wy < n and 0 <= x1 < n and 0 <= x2 < n and 0 <= y1 < n and 0 <= y2 < n:
                            if board[wx][wy] != -1 and board[wx][wy] != INF:
                                if board[x1][y1] != -1 and board[x2][y2] != -1:
                                    if board[x2][y2] == INF and board[x1][y1] != INF:
                                        board[i][j] = max(board[x1][y1],board[wx][wy])+1
                                        board[x2][y2] = board[i][j]
                                    elif board[x1][y1] == INF and board[x2][y2] != INF:
                                        board[i][j] = max(board[x2][y2],board[wx][wy])+1
                                        board[x1][y1] = board[i][j]
                                    elif board[x1][y1] != INF and board[x2][y2] != INF:
                                        board[i][j] = max(board[x1][y1],board[x2][y2],board[wx][wy])+1

def solution(board):
    n = len(board)
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                board[i][j] = -1
                
    for i in range(n):
        for j in range(n):
            if board[i][j] == 0:
                board[i][j] = INF

    board[0][0] = 0
    board[0][1] = 0

    while board[n-1][n-1] == INF:
        bfs(board)
            
    for i in range(n):
        for j in range(n):
            if board[i][j] == INF:
                board[i][j] = -2
    for i in range(n):
        print(board[i])

    return board[n-1][n-1]