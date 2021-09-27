# Q091.py
# https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    num = sum(range(1, len(triangle)+1))

    d = [0] * num
    now = 0
    d[now] = triangle[0][0]
    
    for i in range(len(triangle)-1):
        for j in range(len(triangle[i])):
            child = now + len(triangle[i])
            d[child] = max(d[child], triangle[i+1][j] + d[now])
            child2 = child + 1
            d[child2] = max(d[child2], triangle[i+1][j+1] + d[now])
            now += 1
            
    return max(d)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))