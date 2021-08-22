# Q051.py
# 경쟁적 감염
# https://www.acmicpc.net/problem/18405
import copy
from collections import deque

def infect(array, virus, x, y, now, s):
    n = len(array)
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    for i in range(4):
        a = x + dx[i]
        b = y + dy[i]
        if a >= 0 and b >= 0 and a < n and b < n and array[a][b] == 0:
            array[a][b] = now
            virus.append((a, b, now, s+1))

n, k = map(int, input().split())
array = []
virus = deque()

for _ in range(n):
    array.append(list(map(int, input().split())))

for i in range(1, k+1):
    for a in range(n):
        for b in range(n):
            if array[a][b] == i:
                virus.append((a,b,i,0))

s, x, y = map(int, input().split())

for time in range(s):
    next_array = copy.deepcopy(array)
    if len(virus) == 0:
        break
    while virus[0][3] == time:
        a, b, i, sec = virus.popleft()
        infect(next_array, virus, a, b, i, time)
        if len(virus) == 0:
            break
    array = copy.deepcopy(next_array)

print(array[x-1][y-1])

"""
예제 입력 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2

예제 출력 1 
3

예제 입력 2 
3 3
1 0 2
0 0 0
3 0 0
1 2 2

예제 출력 2 
0
"""