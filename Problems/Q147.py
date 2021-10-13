# Q147.py
# https://www.acmicpc.net/problem/10828

import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    query = input().rstrip()
    if 'push' in query:
        query, num = query.split()
        stack.append(num)
    elif query == 'pop':
        print(-1) if not len(stack) else print(stack.pop())
    elif query == 'size':
        print(len(stack))
    elif query == 'empty':
        print(1) if not len(stack) else print(0)
    else:
        print(-1) if not len(stack) else print(stack[len(stack) - 1])