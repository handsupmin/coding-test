# BFS.py
# Breadth First Search, 너비 우선 탐색

# 1. 탐색 시작 노드를 큐에 합입하고 방문 처리를 한다.
# 2. 큐에서 노드를 꺼내 해당 노드의 인접 노드 중에서 방문하지 않은 노드를 모두 큐에 삽입 하고 방문 처리를 한다.
# 3. 2번의 과정을 더 이상 수행할 수 없을 때까지 반복한다.

# 재귀 함수로 수행되는 DFS 보다 조금 더 빠르게 동작한다.

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while(queue):
        v = queue.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True

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

# 1차원 리스트 초기화
visited = [False] * 9

bfs(graph, 1, visited)