# Q090.py
# https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

import copy

def solution(N, stages):
    clear = [0] * (N + 2)
    fail_rate = []
    
    for stage in stages:
        for i in range(1, stage):
            clear[i] += 1
            
    arrive = copy.deepcopy(clear)
    
    for stage in stages:
        arrive[stage] += 1
        
    for j in range(1, N+1):
        if arrive[j] == 0:
            fail_rate.append((0, j))
        else:
            fail_rate.append(((arrive[j] - clear[j])/arrive[j], j))
        
    fail_rate.sort(reverse = True, key = lambda x: (x[0], -x[1]))
    
    answer = []
    for value in fail_rate:
        answer.append(value[1])
    
    return answer