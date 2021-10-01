# Q098.py
# https://www.acmicpc.net/problem/1149

n = int(input())

street = [[]]

for _ in range(n):
    street.append(list(map(int, input().split())))

d = [[0] * 3 for _ in range(n + 1)]
d[1][0] = street[1][0]
d[1][1] = street[1][1]
d[1][2] = street[1][2]

for i in range(2, n+1):
    d[i][0] = min(d[i-1][1], d[i-1][2]) + street[i][0]
    d[i][1] = min(d[i-1][0], d[i-1][2]) + street[i][1]
    d[i][2] = min(d[i-1][1], d[i-1][0]) + street[i][2]

print(min(d[n]))