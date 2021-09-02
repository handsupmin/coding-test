# Q066.py
# https://programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    q = []
    count = 0
    
    for food in scoville:
        heapq.heappush(q, food)
        
    while q:
        first = heapq.heappop(q)
        if first >= K:
            return count
        else:
            if len(q) == 0:
                break
            count += 1
            second = heapq.heappop(q)
            heapq.heappush(q, first+ (second * 2))
        
    return -1