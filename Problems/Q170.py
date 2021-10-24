# Q170.py
# https://www.acmicpc.net/problem/7576

from collections import deque

m, n = map(int, input().split())
boxes = []
DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    boxes.append(list(map(int, input().split())))

queue = deque()
next_queue = []
count_day = 0
is_it_posible = True
is_there_unripe = False

for i in range(n):
    for j in range(m):
        if boxes[i][j] == 1:
            queue.append((i, j))
        elif boxes[i][j] == 0:
            is_there_unripe = True

if not is_there_unripe:
    print(0)
else:
    while queue:
        while queue:
            x, y = queue.popleft()
            for dx, dy in DELTA:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and boxes[nx][ny] == 0:
                    next_queue.append((nx, ny))
                    boxes[nx][ny] = 1
        if not next_queue:
            break
        queue = deque(next_queue)
        next_queue = []
        count_day += 1

    for i in range(n):
        if not is_it_posible:
            break
        for j in range(m):
            if boxes[i][j] == 0:
                is_it_posible = False
                break

    print(count_day) if is_it_posible else print(-1)