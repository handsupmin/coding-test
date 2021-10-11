# Q137.py
# https://www.acmicpc.net/problem/11650

import sys
input = sys.stdin.readline

array = []

for _ in range(int(input())):
    a, b = map(int, input().split())
    array.append((a, b))

for a, b in sorted(array, key = lambda x : (x[0], x[1])):
    print(a, b)