# Q151.py
# https://www.acmicpc.net/problem/11866

n, k = map(int, input().split())

count = 0
now = 1
result = []
done = [0] * (n + 1)

while len(result) != n:
    if now > n:
        now = 1
    if done[now] == 0:
        count += 1
    if count == k:
        result.append(now)
        done[now] = 1
        count = 0
    now += 1

print(str(result).replace('[', '<').replace(']', '>'))