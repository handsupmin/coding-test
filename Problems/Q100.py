# Q100.py
# https://www.acmicpc.net/problem/1753

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

v, e = map(int, input().split())
start = int(input())

graph = [[] for _ in range(v + 1)]
visited = [False] * (v + 1)
distance = [INF] * (v + 1)

for _ in range(e):
    v1, v2, dist = map(int, input().split())
    graph[v1].append((v2, dist))

for i in range(1, v + 1):
    graph[i].sort(key = lambda x : (x[0], x[1]))

distance[start] = 0
q = []
heapq.heappush(q, (0, start))
while q:
    d, now = heapq.heappop(q)
    if visited[now] == True:
        continue
    visited[now] = True

    for node, dist in graph[now]:
        if visited[node] == False and distance[node] > d + dist:
            distance[node] = d + dist
            heapq.heappush(q, (distance[node], node))

for i in range(1, len(distance)):
    d = distance[i]
    if d == INF:
        print("INF")
    else:
        print(d)