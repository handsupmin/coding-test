# Q068.py
# https://programmers.co.kr/learn/courses/30/lessons/42628

import heapq

def solution(operations):
    q = []
    p = []
    for value in operations:
        oper, num = value.split()
        if oper == 'I':
            heapq.heappush(q, int(num))
        elif oper == 'D':
            if len(q) == 0:
                continue
            if int(num) == 1:
                n = len(q)
                for _ in range(n):
                    heapq.heappush(p, -heapq.heappop(q))
                heapq.heappop(p)
                n = len(p)
                for _ in range(n):
                    heapq.heappush(q, -heapq.heappop(p))
                    
            if int(num) == -1:
                heapq.heappop(q)
                
    if len(q) == 0:
        return [0,0]
    else:
        mini = heapq.heappop(q)
        n = len(q)
        for _ in range(n):
            heapq.heappush(p, -heapq.heappop(q))
        maxi = heapq.heappop(p)
        return [-maxi,mini]