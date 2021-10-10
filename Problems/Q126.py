# Q126.py
# https://programmers.co.kr/learn/courses/30/lessons/77485

def solution(rows, columns, queries):
    array = [[] for _ in range(rows)]

    def rotate(query):
        minimum = int(1e9)
        x1, y1, x2, y2 = query
        copy_x1 = x1 - 1
        copy_y1 = y1 - 1
        copy_x2 = x2 - 1
        copy_y2 = y2 - 1

        nxt = array[copy_x1][copy_y1]
        
        while copy_y1 != copy_y2:
            now = nxt
            minimum = min(minimum, now)
            nxt = array[copy_x1][copy_y1 + 1]
            array[copy_x1][copy_y1 + 1] = now
            copy_y1 += 1
        
        while copy_x1 != copy_x2:
            now = nxt
            minimum = min(minimum, now)
            nxt = array[copy_x1 + 1][copy_y1]
            array[copy_x1 + 1][copy_y1] = now
            copy_x1 += 1
        
        copy_y1 = y1 - 1
        
        while copy_y1 != copy_y2:
            now = nxt
            minimum = min(minimum, now)
            nxt = array[copy_x1][copy_y2 - 1]
            array[copy_x1][copy_y2 - 1] = now
            copy_y2 -= 1
        
        copy_x1 = x1 - 1
        
        while copy_x1 != copy_x2:
            now = nxt
            minimum = min(minimum, now)
            nxt = array[copy_x2 - 1][copy_y1]
            array[copy_x2 - 1][copy_y1] = now
            copy_x2 -= 1
        
        return minimum

    start = 1
    for i in range(rows):
        for j in range(columns):
            array[i].append(start)
            start += 1
    
    answer = []
    for query in queries:
        answer.append(rotate(query))
    
    return answer