# Q087.py
# https://programmers.co.kr/learn/courses/30/lessons/72413

INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
        
    for i in range(n+1):
        graph[i][i] = 0

    for i, j, k in fares:
        graph[i][j] = k
        graph[j][i] = k

    for k in range(1,n+1):
        for i in range(1, n+1):
            if k != i:
                for j in range(1, n+1):
                    if j != i:
                        graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    result = INF
    for mid in range(1, n+1):
        result = min(result, graph[s][mid] + graph[mid][a] + graph[mid][b])
    
    return result