import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

def dijkstra(x, y):
    q = []
    start = (W * x) + y
    heapq.heappush(q, (map_list[x][y], x, y))
    distance[start] = 0
    while q:
        dist, x, y = heapq.heappop(q)
        now = (x * W) + y
        if x == 0 or x == (H - 1) or y == 0 or y == (W - 1):
            return dist
        if distance[now] < dist:
            continue
        for dx, dy in delta:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < H and 0 <= ny < W:
                cost = dist + map_list[nx][ny]
                if cost < distance[(nx * W) + ny]:
                    distance[(nx * W) + ny] = cost
                    heapq.heappush(q, (cost, nx, ny))

for _ in range(int(input())):
    K, W, H = map(int, input().split())

    if W <= 2 or H <= 2:
        print(0)
        continue

    cling_on_list = dict()
    for _ in range(K):
        alpa, cost = input().split()
        cling_on_list[alpa] = cost
    map_list = []
    MAP_SIZE = W * H
    delta = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    
    distance = [INF] * MAP_SIZE

    for i in range(H):
        temp_array = []
        for enemy in list(map(str, input().rstrip())):
            if enemy == 'E':
                start = [i, (len(temp_array))]
                temp_array.append(0)
            else:
                temp_array.append(int(cling_on_list[enemy]))
        map_list.append(temp_array)


    visited = [[False] * W for _ in range(H)]
    print(dijkstra(start[0], start[1]))