# Q181.py
# https://www.acmicpc.net/problem/11726

n = int(input())

d = [0] * (n + 1)

if n == 1:
    print(1)
elif n == 2:
    print(2)
else:
    d[1] = 1
    d[2] = 2

    for i in range(3, n + 1):
        d[i] = d[i - 1] + d[i - 2]
    print(d[n] % 10007)