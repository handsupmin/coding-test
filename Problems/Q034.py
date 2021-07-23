import copy

def solution(key, lock):    
    size = len(lock)
    
    temp = [[0] * size for _ in range(size)]
    if len(key) < size:
        for i in range(len(key)):
            for j in range(len(key)):
                temp[i][j] = key[i][j]
        key = copy.deepcopy(temp)

    for rota in range(4):
        for down in range(size):
            for up in range(size):
                for right in range(size):
                    for left in range(size):
                        result_key = copy.deepcopy(key)
                        for _ in range(rota):
                            result_key = rotate(result_key)
                        for _ in range(down):
                            result_key = move(result_key, 1)
                        for _ in range(up):
                            result_key = move(result_key, 2)
                        for _ in range(right):
                            result_key = move(result_key, 3)
                        for _ in range(left):
                            result_key = move(result_key, 4)
                        if solve(result_key, lock):
                            return True
        
    return False

def rotate(array):
    size = len(array)    
    result = [[0] * size for x in range(size)]    
    for i in range(size):
        for j in range(size):
            result[j][size-i-1] = array[i][j]
    return result

def solve(key, lock):
    size = len(lock)
    count = 0
    for i in range(size):
        for j in range(size):
            if (key[i][j] + lock[i][j]) == 1:
                count += 1
    if count == size * size:
        return True
    else:
        return False
        
def move(array, side):
    # 1: 밑, 2: 위, 3: 오른쪽, 4: 왼쪽으로 이동    
    size = len(array)
    result = [[0] * size for _ in range(size)]
    if side == 1:
        for i in range(size-1):
            result[size-1-i] = array[size-2-i]
        for j in range(size):
            result[0][j] = 0
        return result

    if side == 2:
        for i in range(size-1):
            result[i] = array[i+1]
        for j in range(size):
            result[size-1][j] = 0
        return result

    if side == 3:
        for i in range(size):
            for j in range(size-1):
                result[i][j+1] = array[i][j]
        return result

    if side == 4:
        for i in range(size):
            for j in range(size-1):
                result[i][j] = array[i][j+1]
        return result