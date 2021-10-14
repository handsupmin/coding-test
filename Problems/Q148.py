# Q148.py
# https://www.acmicpc.net/problem/10845

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

queue = deque()
for _ in range(n):
    query = input().rstrip()
    if 'push' in query:
        query, num = query.split()
        queue.append(num)
    elif query == 'pop':
        print(-1) if not len(queue) else print(queue.popleft())
    elif query == 'size':
        print(len(queue))
    elif query == 'empty':
        print(1) if not len(queue) else print(0)
    elif query == 'front':
        print(-1) if not len(queue) else print(queue[0])
    else:
        print(-1) if not len(queue) else print(queue[len(queue) - 1])