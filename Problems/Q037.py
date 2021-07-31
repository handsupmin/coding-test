# Q037.py
# 치킨 배달
from itertools import combinations
from typing import MappingView

def calc(houses, chickens):
    result = 0
    for home in houses:
        minimum = 100000
        h1 = home[0]
        h2 = home[1]
        for chicken in chickens:
            c1 = chicken[0]
            c2 = chicken[1]
            minimum = min([abs(h1 - c1) + abs(h2 - c2), minimum])
        result += minimum
    return result


n, m = map(int,input().split())

chickens = []
houses = []
chicken_distance = []

city = []
for _ in range(n):
    city.append(list(map(int, input().split())))

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            houses.append((i+1, j+1))
        elif city[i][j] == 2:
            chickens.append((i+1, j+1))

if m == len(chickens):
    print(calc(houses, chickens))
else:
    minimum = 10000000
    comb = list(combinations(chickens, m))
    for value in comb:
        minimum = min([calc(houses, value), minimum])
    print(minimum)



"""
입력 예시 1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

출력 예시 1
5

입력 예시 1
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

출력 예시 1
10

입력 예시 1
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

출력 예시 1
11
"""