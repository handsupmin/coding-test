# Q198.py
# https://www.acmicpc.net/problem/1389

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int,input().split())
results = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, n + 1):
    queue = deque([i])
    visited = [False] * (n + 1)
    visited[i] = True
    count = 0
    
    while queue:
        count += 1
        for _ in range(len(queue)):
            now = queue.popleft()

            for nxt in graph[now]:
                if not visited[nxt]:
                    queue.append(nxt)
                    visited[nxt] = True
                    results[i] += count

print(results.index(min(results[1:])))