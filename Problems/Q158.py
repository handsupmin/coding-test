# Q158.py
# https://www.acmicpc.net/problem/2839

target = int(input())

d = [10000] * 5001
d[3] = 1
d[5] = 1
now = 6
while now < 5001:
    if d[now - 3] != 10000:
        d[now] = min(d[now], d[now - 3] + 1)
    if d[now - 5] != 10000:
        d[now] = min(d[now], d[now - 5] + 1)
    now += 1

print(-1) if d[target] == 10000 else print(d[target])