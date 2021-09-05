# Q081.py
#

def solution(N, number):
    d = [0] * 32001
    
    if N != 1:
        for i in range(1, N):
            d[i] = i+1
        d[N] = 1
    else:
        d[1] = 1
    
    for i in range(N+1, number+1):
        cases = set()
        if i % N == 0 and d[i - N] != 0:
            cases.add(d[i - N] + 1)
        cases.add(d[i-1] + d[1])
        if i // 11 > 0:
            cases.add((i // 11)*2 + 1 + (i % 11))
        if i // 111 > 0:
            cases.add((i // 111)*2 + 1 + (i % 111))
        if i // 1111 > 0:
            cases.add((i // 1111)*2 + 1 + (i % 1111))
        if i // 11111 > 0:
            cases.add((i // 11111)*2 + 1 + (i % 11111))
        d[i] = min(cases)
    print(d[:number+1])
    answer = d[number]
    if answer > 8:
        return -1
    else:
        return answer

print(solution(1,1121),7)
"""
print(solution(5,12),4)
print(solution(2,11),3)
print(solution(5,5),1)
print(solution(5,10),2)
print(solution(5,31168),-1)
print(solution(5,1010),7)
print(solution(3,4),3)
print(solution(5,5555),4)
print(solution(5,5550),5)
print(solution(5,20),3)
print(solution(5,30),3)
print(solution(6,65),4)
print(solution(5,2),3)
print(solution(5,4),3)
print(solution(1,1),1)
print(solution(1,11),2)
print(solution(1,111),3)
print(solution(1,1111),4)
print(solution(1,11111),5)
print(solution(7,7776),6)
print(solution(7,7784),5)
print(solution(2,22222),5)
print(solution(2,22223),7)
print(solution(2,22224),6)
print(solution(2,11111),6)
print(solution(2,11),3)
print(solution(2,111),4)
print(solution(2,1111),5)
print(solution(9,36),4)
print(solution(9,37),6)
print(solution(9,72),3)
print(solution(3,18),3)
print(solution(2,1),2)
print(solution(4,17),4)
"""