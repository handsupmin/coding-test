# Q228.py
# 

from collections import deque

def is_in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def add_eatable_fishes(now_size):
    canEat.append(fishes[now_size - 1])
    
def calc_distance(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)
    
def update_distance(x, y):
    dist_index = 2
    for fish in can_eat:
        f_x, f_y, dist = fish
        fish[dist_index] = calc_distance(x, y, f_x, f_y)
    can_eat.sort(key = lambda x : (x[2], x[0], x[1]))

n = int(input())
case = []
fishes = [] * 7
can_eat = deque()
now_size = 2

for _ in range(n):
    case.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        now = case[i][j]
        if now == 9:
            start = [i, j]
        elif now == 0:
            continue
        else:
            fishes[now].append([i, j, 0])

if len(fishes[1]) == 0:
    print(0)
else:
    now = start
    add_eatable_fishes(now_size)
    eat_count = 0
    move_count = 0
    DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    while len(can_eat) != 0:
        now_x, now_y = now
        update_distance(now_x, now_y)
        target_x, target_y, dist = can_eat.popleft()
        
        visited = set()
        queue = deque([now_x, now_y])
        is_found = False
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in DELTA:
                nx = x + dx
                ny = y + dy

                if is_in_range(nx, ny) and (nx, ny) not in visited:
                    if nx == target_x and ny == target_y:
                        now = (target_x, target_y)
                        move_count += dist
                        is_found = True                        
                        eat_count += 1                        
                        if eat_count == now_size:
                            eat_count = 0
                            now_size += 1
                            add_eatable_fishes(now_size)                        
                        break