# Q176.py
# https://www.acmicpc.net/problem/1931

import sys
input = sys.stdin.readline

n = int(input())

meetings = []
count = 0

for _ in range(n):
    meetings.append(list(map(int, input().split())))

meetings.sort(key = lambda x : (x[1], x[0]))
now_start, now_end = 0, 0

for start, end in meetings:
    if start >= now_end:
        now_start = start
        now_end = end
        count += 1

print(count)