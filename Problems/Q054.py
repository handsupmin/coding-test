# Q054.py
# https://programmers.co.kr/learn/courses/30/lessons/42586

from collections import deque

def solution(progresses, speeds):
    q = deque()
    s = deque()
    answer = []
    for n in progresses:
        q.append(n)
    for n in speeds:
        s.append(n)
    
    while q:
        for i in range(len(s)):
            q[i] += s[i]
        
        count = 0
        if q[0] >= 100:
            while q:
                v = q.popleft()
                w = s.popleft()
                if v < 100:
                    q.appendleft(v)
                    s.appendleft(w)
                    break
                count += 1
            answer.append(count)    
    
    return answer