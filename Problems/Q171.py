# Q171.py
# https://www.acmicpc.net/problem/11724

import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

queue = deque()
count = 0

for i in range(1, n + 1):
    if visited[i] == True:
        continue
    count += 1
    queue.append(i)
    visited[i] = True
    while queue:
        now = queue.popleft()
        for nxt in graph[now]:
            if visited[nxt] != True:
                queue.append(nxt)
                visited[nxt] = True

print(count)