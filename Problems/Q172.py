# Q172.py
# https://www.acmicpc.net/problem/1764

import sys
input = sys.stdin.readline

n, m = map(int, input().split())

cant_listen = set()
result = []

for _ in range(n):
    cant_listen.add(input().rstrip())

for _ in range(m):
    name = input().rstrip()
    if name in cant_listen:
        result.append(name)

result.sort()
print(len(result))
if len(result) != 0:
    for name in result:
        print(name)