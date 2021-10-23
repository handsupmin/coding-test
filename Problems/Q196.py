# Q196.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-queue-using-two-stacks/submissions/code/239731483

from collections import deque

queue = deque()
for _ in range(int(input())):
    query = input().split()
    if len(query) == 2:
        queue.append(int(query[1]))
    elif query[0] == '2':
        queue.popleft()
    else:
        if len(queue) != 0:
            print(queue[0])