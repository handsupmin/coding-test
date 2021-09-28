# Q093.py
# https://www.acmicpc.net/problem/1016

import math

min, max = map(int, input().split())

is_true = [True] * (max - min + 1)

for i in range(2, 1000000):
    if i > max:
        break
    j = math.ceil(min / (i * i))
    while (i * i) * j <= max:
        is_true[(i * i) * j - min] = False
        j += 1

print(is_true.count(True))