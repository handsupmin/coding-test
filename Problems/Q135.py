# Q135.py
# https://www.acmicpc.net/problem/11725

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while(queue):
        v = queue.popleft()

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                root[i] = v
                visited[i] = True

n = int(input())

visited = [False] * (n + 1)
root = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]

for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs(graph, 1, visited)

for i in range(2, n + 1):
    print(root[i])