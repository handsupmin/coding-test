# Test.py
# 실험용 파일입니다.
from queue import deque

def dfs(graph, v, visited):
    visited[v] = True
    print(v, end = " ")

    for x in graph[v]:
        if not visited[x]:
            dfs(graph, x, visited)

def bfs(graph, start, visited):
    queue = deque()
    queue.append(start)
    visited[start] = True
    while(queue):
        a = queue.popleft()
        print(a, end = " ")
        for x in graph[a]:
            if not visited[x]:
                queue.append(x)
                visited[x] = True
    

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, 1, visited)

print("\n")
visited = [False] * 9

bfs(graph, 1, visited)