# Q082.py
# 미래 도시

INF = int(1e9)
n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1,n + 1):
    graph[i][i] = 0

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = map(int, input().split())

for now in range(1,n + 1):
    for i in range(1,n + 1):
        for j in range(1,n + 1):
            if i != now and i != j:
                graph[i][j] = min(graph[i][j], graph[i][now] + graph[now][j])

result = graph[1][k] + graph[k][x]

if result > INF:
    result = -1

print(result)

"""
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

3

4 2
1 3
2 4
3 4

-1
"""