# Q206.py
# https://www.acmicpc.net/problem/2178

from collections import deque

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def is_it_path(x, y):
    return maze[x][y] == 1

def is_it_ok(x, y):
    return is_in_range(x, y) and is_it_path(x, y)

def is_it_end(x, y):
    return x == n - 1 and y == m - 1

def bfs(x, y):
    queue = deque([(x, y)])
    while queue:
        x, y = queue.popleft()
        
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy

            if is_it_ok(nx, ny):
                queue.append((nx, ny))
                maze[nx][ny] = maze[x][y] + 1
                if is_it_end(nx, ny):
                    return

n, m = map(int, input().split())

maze = []

for _ in range(n):
    maze.append(list(map(int, input())))

delta = ((0, 1), (0, -1), (1, 0), (-1, 0))
bfs(0, 0)
print(maze[n-1][m-1])