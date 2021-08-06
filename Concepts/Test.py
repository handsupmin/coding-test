# Test.py
# 실험용 파일입니다.

import heapq

def solution(operations):
    q = []
    for value in operations:
        oper, num = value.split()
        if oper == 'I':
            heapq.heappush(q, int(num))
        elif oper == 'D':
            if len(q) == 0:
                continue
            if int(num) == 1:
                q = heapq.nlargest(len(q), q)[1:]
                heapq.heapify(q)
            if int(num) == -1:
                heapq.heappop(q)
    if len(q) == 0:
        return [0,0]
    else:
        return [q[len(q)-1],q[0]]

print(solution(	["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))