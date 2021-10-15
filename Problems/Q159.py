# Q159.py
# https://www.acmicpc.net/problem/7568

import sys
input = sys.stdin.readline

n = int(input())

data = []
counts = []
ranks = [0] * n

for _ in range(n):
    x, y = map(int,input().split())
    data.append((x, y))

for i in range(n):
    count = 0
    for j in range(n):
        if i == j:
            continue
        if data[i][0] < data[j][0] and data[i][1] < data[j][1]:
            count += 1
    ranks[i] = count + 1

print(str(ranks)[1:-1].replace(',', ''))