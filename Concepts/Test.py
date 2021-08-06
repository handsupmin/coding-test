# Test.py
# 실험용 파일입니다.

# Test.py
# 실험용 파일입니다.

def solution(n, build_frame):
    
    answer = []
    column = [[0] * (n+1) for _ in range(n+1)] # 기둥
    row = [[0] * (n+1) for _ in range(n+1)] # 보
    
    for value in build_frame:
        x, y, a, b = value
        if a == 0 and b == 1: # 기둥 설치
            if check_column(column, row, x, y):
                column[y][x] = 1
        
        elif a == 1 and b == 1: # 보 설치
            if check_row(column, row, x, y):
                row[y][x] = 1
            
        elif a == 0 and b == 0: # 기둥 삭제
            column[y][x] = 0
            if not check_delete(column, row, x, y):
                column[y][x] = 1
            
        else: # 보 삭제
            row[y][x] = 0
            if not check_delete(column, row, x, y):
                row[y][x] = 1

    for i in range(n+1):
        for j in range(n+1):
            if column[j][i] == 1:
                answer.append([i,j,0])
            if row[j][i] == 1:
                answer.append([i,j,1])
    
    
    return answer

def check_column(column, row, x, y):
    if y == 0:
        return True
    elif column[y-1][x] == 1:
        return True
    elif row[y][x] == 1:
        return True
    elif row[y][x-1] == 1:
        return True
    return False

def check_row(column, row, x, y):
    if column[y-1][x] == 1:
        return True
    elif column[y-1][x+1] == 1:
        return True
    elif row[y][x-1] == 1 and row[y][x+1] == 1:
        return True
    return False

def check_delete(column, row, x, y):
    n = len(column)
    for i in range(n):
        for j in range(n):
            if column[j][i] == 1 and not check_column(column, row, i, j):
                return False
            if row[j][i] == 1 and not check_row(column, row, i, j):                
                return False
    return True

print(solution(5,	[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))
