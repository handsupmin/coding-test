# Q209.py
# https://www.acmicpc.net/problem/11727

n = int(input())
d = [0] * (n + 1)

d[1] = 1
d[2] = 3

if 1 <= n <= 2:
    print(d[n])

else:
    for i in range(3, n + 1):
        d[i] = d[i - 1] + (d[i - 2] * 2)
    print(d[n] % 10007)