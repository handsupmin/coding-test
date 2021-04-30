# Q010.py

"""
미로 탈출
N x M 크기의 직사각형 형태의 미로에서 통로는 1 벽은 0이다.
한번에 한 칸씩 이동할 수 있으며, 시작 위치는 (1,1)이다.
미로는 반드시 탈출할 수 있는 형태로 제시된다.
시작 칸과 마지막 칸을 포함해서 계산할 때, 탈출을 위해 움직여야 하는 최소 칸의 개수를 구하시오.
"""

from collections import deque

n, m = map(int, input().split())

graph = []

for i in range(n):
    graph.append(list(map(int, input())))

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs(x,y):
    queue = deque()
    queue.append((x,y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] += graph[x][y]
                queue.append((nx, ny))
    
    print(graph[n-1][m-1])
    return

bfs(0,0)

"""
5 7
1010101
1111111
0000011
1111111
1111111
"""
    