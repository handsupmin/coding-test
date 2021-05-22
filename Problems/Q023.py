# Q023.py
# 도시 분할 계획
"""
마을은 N개의 집과 그 집들을 연결하는 M개의 길로 이루어져 있다. 길은 어느 방향으로든지 다닐 수 있으며 각 길마다 유지비가 있다.
마을의 이장은 마을을 2개의 분리된 마을로 분할할 계획을 세우고 있다.
각 마을에는 적어도 하나 이상의 집이 있어야 하고, 분리된 마을 안에 있는 임의의 두 집 사이에 경로가 항상 존재해야 한다.
길은 없앨 수 있으며, 위 조건을 만족하도록 길들을 모두 없애고 나머지 길의 유지비의 합을 최소로 하는 프로그램을 작성하시오.
"""
def find_parent(parent, a):
    if parent[a] != a:
        parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a > b:
        parent[b] = parent[a]
    else:
        parent[a] = parent[b]

n, m = map(int, input().split())
parent = [0] * (n + 1)

t = []
result = 0

graph = []

for _ in range(m):
    a, b, cost = map(int, input().split())
    graph.append((cost, a, b))

for i in range(1, n + 1):
    parent[i] = i

graph.sort()

for j in graph:
    cost, a, b = j
    if find_parent(parent, a) != find_parent(parent, b):
        union(parent, a, b)
        t.append(cost)

t.sort()
result = sum(t[:-1])
print(result)
"""
입력 예시
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

출력 예시
8
"""