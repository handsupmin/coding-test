# Q228.py
# https://www.acmicpc.net/problem/16236

from collections import deque

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

n = int(input())
case = []
fishes = [[] for _ in range(7)]
now_size = 2

for _ in range(n):
    case.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if case[i][j] == 9:
            start = (i, j)
            case[i][j] = 0

now = start
eat_count = 0
move_count = 0
DELTA = [(-1, 0), (0, -1), (0, 1), (1, 0)]

while True:
    now_x, now_y = now
    visited = set((now_x, now_y))
    queue = deque([(now_x, now_y, 0)])
    fish_list = []
    
    while queue:
        x, y, now_count = queue.popleft()        
        for dx, dy in DELTA:
            nx = x + dx
            ny = y + dy
            if is_in_range(nx, ny) and (nx, ny) not in visited:
                if 0 < case[nx][ny] < now_size:
                    fish_list.append((nx, ny, now_count + 1))
                    visited.add((nx, ny))
                    continue
                elif case[nx][ny] <= now_size:
                    queue.append((nx, ny, now_count + 1))
                    visited.add((nx, ny))
    if len(fish_list) == 0:
        break
    else:
        fish_list.sort(key = lambda x : (x[2], x[0], x[1]))
        nx, ny, now_count = fish_list[0]
        case[nx][ny] = 0
        now = (nx, ny)
        move_count += now_count
        eat_count += 1
        if eat_count == now_size:
            eat_count = 0
            now_size += 1
        continue

print(move_count)