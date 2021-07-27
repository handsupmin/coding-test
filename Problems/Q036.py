# Q036.py
# 기둥과 보
# https://programmers.co.kr/learn/courses/30/lessons/60061?language=python3

def solution(n, build_frame):
    column = [[0] * (n + 1) for _ in range(n+1)]
    tile = [[0] * (n + 1) for _ in range(n+1)]
    
    x, y, a, b = 0, 0, 0, 0

    for value in build_frame:
        x, y, a, b = map(int, value)
        
        if a == 0 and b == 1: # 기둥을 설치하는 경우
            if check_column(x, y, column, tile):
                column[y][x] = 1
        elif a == 1 and b == 1: # 보를 설치하는 경우
            if check_tile(x, y, column, tile):
                tile[y][x] = 1
        elif a == 0 and b == 0: # 기둥을 삭제하는 경우
            column[y][x] = 0
            if check_delete(x, y, column, tile):
                column[y][x] = 1
        elif a == 1 and b == 0: # 보를 삭제하는 경우
            tile[y][x] = 0
            if check_delete(x, y, column, tile):
                tile[y][x] = 1
    
    result = []
    for x in range(n+1):
        for y in range(n+1):
            if column[y][x] == 1:
                result.append([x, y, 0])
            if tile[y][x] == 1:
                result.append([x, y, 1])
    
    return result

def check_column(x, y, column, tile):
    if y == 0:
        return True
    elif column[y-1][x] == 1:
        return True
    elif tile[y][x-1] == 1 or tile[y][x] == 1:
        return True
    else:
        return False

def check_tile(x, y, column, tile):
    if column[y-1][x] == 1 or column[y-1][x+1] == 1:
        return True
    elif tile[y][x-1] == 1 and tile[y][x+1] == 1:
        return True
    else:
        return False

def check_delete(x, y, column, tile):
    n = len(column)
    for i in range(n):
        for j in range(n):
            if column[j][i] == 1 and not check_column(i, j, column, tile):
                return True
            if tile[j][i] == 1 and not check_tile(i, j, column, tile):
                return True
    return False