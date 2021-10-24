# Q164.py
# https://www.acmicpc.net/problem/1012

import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def _is_in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def _is_it_cabbage(x, y):
    return field[x][y] == 1

def is_it_ok(x, y):
    return _is_in_range(x, y) and _is_it_cabbage(x, y)

for _ in range(t):
    m, n, k = map(int, input().split())

    field = [[0] * m for _ in range(n)]
    queue = deque()
    count = 0

    for _ in range(k):
        x, y = map(int, input().split())
        field[y][x] = 1
    

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                count += 1
                queue.append((i, j))
                field[i][j] = 0
                while queue:
                    x, y = queue.popleft()
                    
                    for dx, dy in DELTA:
                        nx = x + dx
                        ny = y + dy
                        
                        if is_it_ok(nx, ny):
                            queue.append((nx, ny))
                            field[nx][ny] = 0
    
    print(count)