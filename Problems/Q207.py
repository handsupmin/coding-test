# Q207.py
# https://www.acmicpc.net/problem/2667

from collections import deque

n = int(input())

aparts = []
kind_of_aparts = 0
num_of_aparts = []
now = 1
delta = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(n):
    aparts.append(list(map(int, input())))

visited = set()

for i in range(n):
    for j in range(n):
        if aparts[i][j] == 1 and (i, j) not in visited:
            queue = deque([(i, j)])
            visited.add((i, j))
            kind_of_aparts += 1
            count_of_apart = 1

            while queue:
                x, y = queue.popleft()

                for dx, dy in delta:
                    nx = x + dx
                    ny = y + dy

                    if 0 <= nx < n and 0 <= ny < n and aparts[nx][ny] == 1 and (nx, ny) not in visited:
                        visited.add((nx, ny))
                        queue.append((nx, ny))
                        count_of_apart += 1
            
            num_of_aparts.append(count_of_apart)

num_of_aparts.sort()

print(kind_of_aparts)
for num in num_of_aparts:
    print(num)