# Q045.py
# 특정 거리의 도시 찾기

from collections import deque

n, m, k, x = map(int, input().split())

q = deque()
distance = [1000] * (n+1)
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance[x] = 0

for value in graph[x]:
    q.append(value)
    distance[value] = 1

while q:
    city = q.popleft()
    for i in graph[city]:
        distance[i] = min(distance[i], distance[city] + 1)
        q.append(i)

result = []
for j in range(1, len(distance)):
    if distance[j] == k:
        result.append(j)

if len(result) == 0:
    print(-1)
else:
    for value in result:
        print(value)



"""
입력 예시
4 4 2 1
1 2
1 3
2 3
2 4

출력 예시
4

입력 예시
4 3 2 1
1 2
1 3
1 4

출력 예시
-1

입력 예시
4 4 1 1
1 2
1 3
2 3
2 4

출력 예시
2
3
"""