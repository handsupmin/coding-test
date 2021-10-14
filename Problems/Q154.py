# Q154.py
# https://www.acmicpc.net/problem/2775

t = int(input())

for _ in range(t):
    k = int(input())
    n = int(input())
    down_floor = list(range(1, n + 1))
    up_floor = [0] * n
    for _ in range(1, k + 1):
        for i in range(0, n):
            up_floor[i] = sum(down_floor[:i + 1])
        down_floor = up_floor
        up_floor = [0] * n
    print(down_floor[n - 1])