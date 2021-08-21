# Q050.py
# 연구소
from itertools import combinations
import copy

def infect(lab, x, y):
    if x < 0 or y < 0 or x >= len(lab[0]) or y >= len(lab):
        return
    elif lab[y][x] == 0:
        lab[y][x] = 2        
        infect(lab, x+1, y)
        infect(lab, x-1, y)
        infect(lab, x, y-1)
        infect(lab, x, y+1)
    else:
        return

n, m = map(int, input().split())

wall = []
virus = []
lab = []

for a in range(n):
    lab.append(list(map(int, input().split())))

for a in range(n):
    for b in range(m):
        if lab[a][b] == 0:
            wall.append((a,b))
        if lab[a][b] == 2:
            virus.append((a,b))

candidate = list(combinations(wall, 3))

maximum = 0

for t in candidate:
    temp_map = copy.deepcopy(lab)
    count = 0
    for value in t:
        x = value[1]
        y = value[0]
        temp_map[y][x] = 1
    for v in virus:
        x = v[1]
        y = v[0]
        infect(temp_map, x+1, y)
        infect(temp_map, x-1, y)
        infect(temp_map, x, y+1)
        infect(temp_map, x, y-1)
    for a in range(n):
        for b in range(m):
            if temp_map[a][b] == 0:
                count += 1
    if count > maximum:
        maximum = count

print(maximum)
"""
입력 예시
7 7
2 0 0 0 1 1 0
0 0 1 0 1 2 0
0 1 1 0 1 0 0
0 1 0 0 0 0 0
0 0 0 0 0 1 1
0 1 0 0 0 0 0
0 1 0 0 0 0 0

출력 예시
27

입력 예시
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

출력 예시
9

입력 예시
8 8
2 0 0 0 0 0 0 0 2
2 0 0 0 0 0 0 0 2
2 0 0 0 0 0 0 0 2
2 0 0 0 0 0 0 0 2
2 0 0 0 0 0 0 0 2
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

출력 예시
3
"""