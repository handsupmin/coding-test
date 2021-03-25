# graph.py

# # 그래프를 표현하는 두 가지 방법
# 1. Adjacency Matrix, 인접 행렬
# 메모리 낭비, 시간 절약

INF = 999999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph)

# 2. Adjacency list, 인접 리스트
# 시간 낭비, 메모리 절약

graph = [[] for _ in range(3)]
# 컴프리핸션
# (x, y, z) for x in Iterator for y in Iterator for z in Iterator if _ if _

graph[0].append((1, 7))
graph[0].append((2, 5))

graph[1].append((0, 7))

graph[2].append((0, 5))

print(graph)