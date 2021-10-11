# Q133.py
# https://www.acmicpc.net/problem/2108

import sys
from collections import Counter
input = sys.stdin.readline

def modefinder(numbers):
    c = Counter(numbers)
    order = c.most_common()
    maximum = order[0][1]
    modes = []
    for num in order:
        if num[1] == maximum:
            modes.append(num[0])
    return modes

num_list = []

n = int(input().rstrip())

for _ in range(n):
    num = int(input().rstrip())
    num_list.append(num)

num_list.sort()

mode_list = modefinder(num_list)
mode_list.sort()

print(int(round(sum(num_list)/n, 0)))
print(num_list[n//2])
if len(mode_list) >= 2:
    print(mode_list[1])
else:
    print(mode_list[0])
print(max(num_list) - min(num_list))