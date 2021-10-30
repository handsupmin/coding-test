# 180.py
# https://www.acmicpc.net/problem/11723

import sys
input = sys.stdin.readline
num_set = set()

for _ in range(int(input())):
    query = list(input().split())
    if len(query) == 2:
        func, num = query[0], int(query[1])
        if func == 'add':
            num_set.add(num)
        elif func == 'remove':
            if num in num_set:
                num_set.remove(num)
        elif func == 'check':
            print(1) if num in num_set else print(0)
        elif func == 'toggle':
            num_set.remove(num) if num in num_set else num_set.add(num)
    else:
        if query[0] == 'all':
            num_set = set(list(range(1, 21)))
        else:
            num_set.clear()