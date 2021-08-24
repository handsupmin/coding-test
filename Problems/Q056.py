# Q056.py
# https://programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque(truck_weights)
    time = 0
    now = deque()
    done = []
    while len(done) != len(truck_weights):
        time += 1
        if len(now) > 0:
            if now[0][1] == time:
                done.append(now.popleft())
        if len(q) > 0:
            total = 0
            for i in now:
                total += i[0]
            if (q[0] + total) <= weight:
                t = q.popleft()
                now.append((t, time+bridge_length))
    answer += time
            
    return answer