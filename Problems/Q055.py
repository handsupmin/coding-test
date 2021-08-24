# Q055.py
# https://programmers.co.kr/learn/courses/30/lessons/42587

from collections import deque

def solution(priorities, location):
    q = deque()
    count = 0
    
    for i in range(len(priorities)):
        q.append((priorities[i], i))
    
    while q:
        j = q.popleft()
        if len(q) == 0:
            return len(priorities)
        if j[0] >= max(q)[0]:
            count += 1
            if j[1] == location:
                return count
        else:
            q.append(j)
