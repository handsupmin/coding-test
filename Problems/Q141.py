# Q141.py
# https://www.acmicpc.net/problem/2798

from itertools import combinations

result = []
n, m = map(int, input().split())
for a, b, c in list(combinations(list(map(int, input().split())), 3)):
    if (a + b + c) <= m:
        result.append(a + b + c)

print(max(result))