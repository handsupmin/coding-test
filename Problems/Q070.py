# Q070.py
# https://programmers.co.kr/learn/courses/30/lessons/43162

from collections import deque

def solution(n, computers):
    DISCONNECTED, CONNECTED = range(2)
    connected_computers = [[] for _ in range(n)]
    visited = set()
    
    for i in range(len(computers)):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                connected_computers[i].append(j)
    q = deque([])
    count = 0
    
    for i in range(n):
        if i not in visited:
            visited.add(i)
            q.append(i)
            while q:
                j = q.popleft()
                visited.add(j)
                for computer in connected_computers[j]:
                    if computer not in visited:
                        q.append(computer)
            count += 1
            
    return count