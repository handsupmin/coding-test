# Q173.py
# https://www.acmicpc.net/problem/1927

import heapq
import sys

input = sys.stdin.readline
queue = []
for _ in range(int(input())):
    num = int(input())
    if num == 0 and len(queue) == 0:
        print(0)
    elif num == 0:
        print(heapq.heappop(queue))
    else:
        heapq.heappush(queue, num)