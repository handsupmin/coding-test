# Q036.py

def solution(n, build_frame):
    coloumn = [[-1] * (n + 1) for _ in range(n+1)]
    tile = [[-1] * (n + 1) for _ in range(n+1)]
    
    x, y, a, b = 0, 0, 0, 0

    for value in build_frame:
        x, y, a, b = map(int, value)
        
        if a == 0 and b == 1: # 기둥을 설치하는 경우
        elif a == 1 and b == 1: # 보를 설치하는 경우
        elif a == 0 and b == 0: # 기둥을 삭제하는 경우
        elif a == 1 and b == 0: # 보를 삭제하는 경우
    
    result = []
    for x in range(n+1):
        for y in range(n+1):
    
    return result

def check_column(x, y, coloumn, tile):
    if y == 0:
        return True
    elif coloumn[y-1][x] == 0:
        return True
def check_tile(x, y, coloumn, tile):

def check_delete(x, y, coloumn, tile):