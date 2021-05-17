# Q021.py
"""
전보
어떤 나라에는 N개의 도시가 있다. 그리고 각 도시는 보내고자 하는 메시지가 잇는 경우, 다른 도시로 전보를 보내서 다른 도시로 해당 메시지를 전송할 수 있다.
하지만 X라는 도시에서 Y라는 도시로 전보를 보내고자 한다면, 도시 X에서 Y로 향하는 통로가 설치되어 있어야 한다. 예를 들어 X에서 Y로 향하는 통로는 있지만,
Y에서 X로 향하는 통로가 없다면 Y는 X로 메시지를 보낼 수 없다. 또한 통로를 거쳐 메시지를 보낼 때는 일정 시간이 소요된다.
어느 날 C라는 도시에서 위급 상황이 발생했다. 그래서 최대한 많은 도시로 메시지를 보내고자 한다.
메시지는 도시 C에서 출발항 각 도시 사이에 설치된 통로를 거쳐, 최대한 많이 퍼져나갈 것이다. 각 도시의 번호와 통로가 설치되어 있는 정보가 주어졌을 때,
도시 C에서 보낸 메시지를 받게 되는 도시의 개수는 총 몇 개이며 도시들이 모두 메시지를 받는 데까지 걸리는 시간은 얼마인지 계산하는 프로그램을 작성하시오.
첫째 줄에 도시의 개수 N, 통로의 개수 M, 메시지를 보내고자 하는 도시 C가 주어진다.
(1 <= N <= 30000, 1 <= M <= 200000, 1 <= C <= N)
둘째 줄부터 M + 1번쨰 줄에 걸쳐서 통로에 대한 정보 X, Y, Z가 주어진다. 이는 특정 도시 X에서 다른 특정 도시 Y로 이어지는 통로가 있으며, 메시지가 전달되는 시간이 Z라는 의미이다.
(1 <= X, Y <= N, 1 <= Z <= 1000)
첫째 줄에 도시 C에서 보낸 메시지를 받는 도시의 총 개수와 총 걸리는 시간을 공백으로 구분하여 출력한다.
"""
import heapq
INF = int(1e9)
# n 노드의 개수, m 간선의 개수, c 시작 노드
n, m, c = map(int, input().split())

graph = [[] for _ in range(n + 1)]

distance = [INF] * (n + 1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

def dijkstra(start, array):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, 0))
    while(q):
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            a, b = i[0], i[1]
            cost = dist + b
            if cost < distance[a]:
                distance[a] = cost
                heapq.heappush(q, (a, cost))

dijkstra(c, graph)


for i in range(1, n + 1):
    # 도달할 수 없는 경우, 무한(INFINITY)이라고 출력
    if distance[i] == INF:
        print("INFINITY")
    # 도달할 수 있는 경유 거리를 출력
    else:
        print(distance[i])

count = 0
dist = 0

for i in range(len(distance)):
    if i != c and distance[i] != INF:
        count += 1
        dist = max(dist, distance[i])
    

print(count, dist)

"""
입력 예시
3 2 1
1 2 4
1 3 2
출력 예시
2 4

6 11 1
1 2 2
1 3 5
1 4 1
2 3 3
2 4 2
3 2 3
3 6 5
4 3 3
4 5 1
5 3 1
5 6 2
출력 예시
5 4
"""