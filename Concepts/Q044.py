# Q044.py
# 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3

def solution(n, weak, dist):
    dist.sort(reverse = True)  
    weak.append(weak[0]+n)
    minimum = 1000
    
    go = []    
    for i in range(len(weak) -1):
        go.append(weak[i+1] - weak[i])        
    go.sort()
    print(dist, go)
    if len(weak) <= len(dist):
        minimum = min(minimum, len(weak))
    
    for j in range(1, len(dist)):
        temp = go[:-(j)]
        if sum(temp) <= sum(dist[:j]):
            minimum = min(minimum, j)

    if minimum >= len(dist):
        return -1
    
    return minimum

print(solution(30, [0, 3, 11, 21], [10, 4]))