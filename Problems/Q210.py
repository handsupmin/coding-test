# Q210.py
# https://www.acmicpc.net/problem/7569

from collections import deque

m, n, h = map(int, input().split())
boxes = []
DELTA = [(0, 0, 1), (0, 0, -1), (0, 1, 0), (0, -1, 0), (1, 0, 0), (-1, 0, 0)]

for _ in range(h):
    box = []
    for _ in range(n):
        box.append(list(map(int, input().split())))
    boxes.append(box)

queue = deque()
next_queue = []
count_day = 0
is_it_posible = True
is_there_unripe = False

for k in range(h):
    for i in range(n):
        for j in range(m):
            if boxes[k][i][j] == 1:
                queue.append((k, i, j))
            elif boxes[k][i][j] == 0:
                is_there_unripe = True

if not is_there_unripe:
    print(0)
else:
    while queue:
        while queue:
            w, x, y = queue.popleft()
            for dw, dx, dy in DELTA:
                nw = w + dw
                nx = x + dx
                ny = y + dy
                if 0 <= nw < h and 0 <= nx < n and 0 <= ny < m and boxes[nw][nx][ny] == 0:
                    next_queue.append((nw, nx, ny))
                    boxes[nw][nx][ny] = 1
        
        if not next_queue:
            break
        queue = deque(next_queue)
        next_queue = []
        count_day += 1

    for k in range(h):
        for i in range(n):
            if not is_it_posible:
                break
            for j in range(m):
                if boxes[k][i][j] == 0:
                    is_it_posible = False
                    break

    print(count_day) if is_it_posible else print(-1)