# Q169.py
# https://www.acmicpc.net/problem/2606

from collections import deque

n = int(input())
m = int(input())

visited = [False] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
queue.append(1)
visited[1] = True
count = 0

while queue:
    now = queue.popleft()
    for nxt in graph[now]:
        if visited[nxt] != True:
            queue.append(nxt)
            visited[nxt] = True
            count += 1

print(count)