# Q083.py
# 전보

import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)
start = (0, c)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start):
    visited = [0] * (n + 1)
    q = []
    heapq.heappush(q, start)
    while q:
        dist, now = heapq.heappop(q)
        visited[now] = 1
        for node, n_dist in graph[now]:
            if visited[node] == 0:
                heapq.heappush(q, (n_dist, node))
                distance[node] = min(distance[node], dist + n_dist)

dijkstra(start)
count = 0
maxi = 0
for i in range(1, n+1):
    if distance[i] != INF:
        count += 1
        maxi = max(maxi, distance[i])

print(count, maxi)
"""
3 2 1
1 2 4
1 3 2

2 4
"""