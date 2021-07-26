# Q036.py

def solution(n, build_frame):
    blue_print = [[-1] * (n + 1) for _ in range(n+1)]
    
    x, y, a, b = 0, 0, 0, 0

    for value in build_frame:
        x, y, a, b = map(int, value)
        
        if a == 0 and b == 1: # 기둥을 설치하는 경우
            if check_column(x, y, blue_print):
                if blue_print[y][x] == 1:
                    blue_print[y][x] = 2
                else:
                    blue_print[y][x] = 0
        elif a == 1 and b == 1: # 보를 설치하는 경우
            if check_tile(x, y, blue_print):
                if blue_print[y][x] == 0:
                    blue_print[y][x] = 2
                else:
                    blue_print[y][x] = 1
        elif a == 0 and b == 0: # 기둥을 삭제하는 경우
            if blue_print[y][x] == 2:
                blue_print[y][x] = 1
                if (blue_print[y+1][x] == 0 or blue_print[y+1][x] == 2) and not check_column(x, y+1, blue_print):
                    blue_print[y][x] = 2
                elif (blue_print[y+1][x-1] == 1 or blue_print[y+1][x-1] == 2) and not check_tile(x-1, y+1, blue_print):
                    blue_print[y][x] = 2
                elif (blue_print[y+1][x] == 1 or blue_print[y+1][x] == 2) and not check_tile(x, y+1, blue_print):
                    blue_print[y][x] = 2
            else:
                blue_print[y][x] = -1
                if (blue_print[y+1][x] == 0 or blue_print[y+1][x] == 2) and not check_column(x, y+1, blue_print):
                    blue_print[y][x] = 0
                elif (blue_print[y+1][x-1] == 1 or blue_print[y+1][x-1] == 2) and not check_tile(x-1, y+1, blue_print):
                    blue_print[y][x] = 0
                elif (blue_print[y+1][x] == 1 or blue_print[y+1][x] == 2) and not check_tile(x, y+1, blue_print):
                    blue_print[y][x] = 0
        elif a == 1 and b == 0: # 보를 삭제하는 경우
            if blue_print[y][x] == 2:
                blue_print[y][x] = 0
                if (blue_print[y][x-1] == 1 or blue_print[y][x-1] == 2) and not check_tile(x-1, y, blue_print):
                    blue_print[y][x] = 2
                elif (blue_print[y][x+1] == 1 or blue_print[y][x+1] == 2) and not check_tile(x+1, y, blue_print):
                    blue_print[y][x] = 2
                elif not check_column(x, y, blue_print):
                    blue_print[y][x] = 2
                elif (blue_print[y][x+1] == 0 or blue_print[y][x+1] == 2) and not check_column(x+1, y, blue_print):
                    blue_print[y][x] = 2
            else:
                blue_print[y][x] = -1
                if (blue_print[y][x-1] == 1 or blue_print[y][x-1] == 2) and not check_tile(x-1, y, blue_print):
                    blue_print[y][x] = 1
                elif (blue_print[y][x+1] == 1 or blue_print[y][x+1] == 2) and not check_tile(x+1, y, blue_print):
                    blue_print[y][x] = 1
                elif (blue_print[y][x+1] == 0 or blue_print[y][x+1] == 2) and not check_column(x+1, y, blue_print):
                    blue_print[y][x] = 1
    
    result = []
    for x in range(n+1):
        for y in range(n+1):
            if blue_print[y][x] != -1:
                if blue_print[y][x] == 2:
                    result.append([x, y, 0])
                    result.append([x, y, 1])
                else:
                    result.append([x, y, blue_print[y][x]])
    
    return result

def check_column(x, y, blue_print):
    if y == 0:
        return True
    elif blue_print[y-1][x] == 0 or blue_print[y-1][x] == 2:
        return True
    elif blue_print[y][x-1] == 1 or blue_print[y][x-1] == 2:
        return True
    elif blue_print[y][x] == 1:
        return True
    else:
        return False

def check_tile(x, y, blue_print):
    if blue_print[y-1][x] == 0 or blue_print[y-1][x+1] == 0:
        return True
    elif blue_print[y-1][x] == 2 or blue_print[y-1][x+1] == 2:
        return True
    elif (blue_print[y][x-1] == 1 or blue_print[y][x-1] == 2) and (blue_print[y][x+1] == 1 or blue_print[y][x+1] == 2):
        return True
    else:
        return False