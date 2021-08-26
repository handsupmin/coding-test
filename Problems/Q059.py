# Q059.py
# https://www.acmicpc.net/problem/16234

from collections import deque

def bfs(i, j):
    border = []
    border.append((i, j))
    q = deque()
    q.append((i, j))

    while q:
        x, y = q.popleft()
        for i in range(4):
            a = x + dx[i]
            b = y + dy[i]
            if 0 <= a < n and 0 <= b < n and visited[a][b] == 0:
                if l <= abs(A[a][b] - A[x][y]) <= r:
                    visited[a][b] = 1
                    border.append((a, b))
                    q.append((a, b))
    return border

n, l, r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

count = 0
while True:
    visited = [[0] * n for _ in range(n)]
    isTrue = False
    for i in range(n):
        for j in range(n):
            if visited[i][j] == 0:
                visited[i][j] = 1
                border = bfs(i, j)
                if len(border) > 1:
                    isTrue = True
                    move = sum([A[x][y] for x, y in border]) // len(border)
                    for x, y in border:
                        A[x][y] = move
    if not isTrue:
        break
    count += 1

print(count)
