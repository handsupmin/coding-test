# Q143.py
# https://www.acmicpc.net/problem/9012

from collections import deque

n = int(input())

for _ in range(n):
    is_it_no = False
    q = deque()
    data = list(input())
    for value in data:
        if value == '(':
            q.append(value)
        elif value == ')' and len(q) != 0:
            q.popleft()
        else:
            is_it_no = True
            break
    if is_it_no or len(q) != 0:
        print("NO")
    else:
        print("YES")