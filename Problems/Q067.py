# Q067.py
# https://programmers.co.kr/learn/courses/30/lessons/42627

from collections import deque
import heapq

def solution(jobs):
    jobs.sort()
    queue = deque(jobs)
    q = []
    TIME = -1
    STATE = 0
    FREE, RUNNING = range(2)
    LEFT_SEC = 0
    RUNNING_TIME = 0
    REQUEST_TIME = 0
    
    count = 0
    
    while True:
        TIME += 1
        
        if STATE == RUNNING:
            LEFT_SEC -= 1
            if LEFT_SEC == 0:
                RUNNING_TIME += TIME - REQUEST_TIME
                STATE = FREE
                count += 1
                
        if len(queue) != 0:
            if STATE == FREE and queue[0][0] <= TIME and len(q) == 0:
                REQUEST_TIME, LEFT_SEC = queue.popleft()
                STATE = RUNNING
                
                
            elif STATE == FREE and len(q) != 0:
                LEFT_SEC, REQUEST_TIME = heapq.heappop(q)
                if queue[0][1] < LEFT_SEC and queue[0][0] <= TIME:
                    heapq.heappush(q, [LEFT_SEC, REQUEST_TIME])
                    REQUEST_TIME, LEFT_SEC = queue.popleft()
                STATE = RUNNING
                    
            elif STATE == RUNNING and queue[0][0] <= TIME:
                j1, j2 = queue.popleft()
                heapq.heappush(q, [j2, j1])
                
        else:
            if STATE == FREE and len(q) == 0:
                break
                
            elif STATE == FREE and len(q) != 0:
                LEFT_SEC, REQUEST_TIME = heapq.heappop(q)
                STATE = RUNNING
    
    return RUNNING_TIME//count