# Q062.py
# 미로 탈출

from collections import deque

def _is_in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def _is_it_open(x, y):
    return maze[x][y] == OPEN

def _is_it_ok(x, y):
    return _is_in_range(x, y) and _is_it_open(x, y)

def yield_found_way(x, y):
    for dx, dy in DELTAS:
        next_x, next_y = x + dx, y + dy
        if _is_it_ok(next_x, next_y):
            yield (next_x, next_y)

MONSTER, OPEN = range(2)
START = (0, 0)
DELTAS = ((0, 1), (0, -1), (1, 0), (-1, 0))
n, m = map(int,input().split())
END_POINT = (n-1, m-1)
maze = []
queue = deque([START])
visited = set()
visited.add(START)

for _ in range(n):
    maze.append(list(map(int,input())))

while queue:
    
    for _ in range(len(queue)):
        x, y = queue.popleft()
        for value in yield_found_way(x, y):
            if value not in visited:
                maze[value[0]][value[1]] += maze[x][y]
                queue.append(value)
                visited.add(value)
                if value == END_POINT:
                    break

x, y = END_POINT
print(maze[x][y])


"""
5 8
10101011
11111111
00100111
11111000
11111111
"""