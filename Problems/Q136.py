# Q136.py
# https://www.acmicpc.net/problem/10989

import sys
from collections import defaultdict
input = sys.stdin.readline

array = defaultdict(int)

for _ in range(int(input())):
    array[int(input())] += 1

for n in sorted(list(array.keys())):
    for _ in range(array[n]):
        print(n)