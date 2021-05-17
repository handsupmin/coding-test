# Q020.py
"""
미래 도시
1번에서 K를 거쳐 X로 가는 최소 시간을 계산하라.
"""
INF = int(1e9)
n, m = map(int, input().split())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(len(graph)):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for i in range(1, len(graph)):
    for j in range(1, len(graph)):
        for k in range(1, len(graph)):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(len(graph)):
    print(graph[i])

if graph[1][k] == INF:
    print(-1)
elif graph[k][x] == INF:
    print(-1)
else:
    print(graph[1][k] + graph[k][x])

"""
입력 예시
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5
출력 예시
3

입력 예시
4 2
1 3
2 4
3 4
출력 예시
-1
"""