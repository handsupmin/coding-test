# Q203.py
# https://www.acmicpc.net/problem/2579

n = int(input())

stairs = []

for _ in range(n):
    stairs.append(int(input()))

if n == 1:
    print(stairs[0])
elif n == 2:
    print(sum(stairs))
elif n == 3:
    print(max(stairs[0] + stairs[2], stairs[1] + stairs[2]))
else:
    d = [0] * n
    d[0] = stairs[0]
    d[1] = stairs[0] + stairs[1]
    d[2] = max(stairs[0] + stairs[2], stairs[1] + stairs[2])
    for i in range(3, n):
        d[i] = max(stairs[i] + d[i-2], stairs[i] + stairs[i-1] + d[i-3])

    print(d[n - 1])