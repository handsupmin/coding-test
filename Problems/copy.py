import copy

def solution(key, lock):    
    size = len(lock)
    
    temp = [[0] * size for _ in range(size)]
    if len(key) < size:
        for i in range(len(key)):
            for j in range(len(key)):
                temp[i][j] = key[i][j]
        key = copy.deepcopy(temp)
    
    if solve(key, lock):
        return True

    rotated_key = copy.deepcopy(key)
    down_key = copy.deepcopy(key)
    up_key = copy.deepcopy(key)
    right_key = copy.deepcopy(key)
    left_key = copy.deepcopy(key)

    for _ in range(4):
        for _ in range(size):
            for _ in range(size):
                right_key = move(right_key, 3)
                if solve(right_key, lock):
                    return True
            for _ in range(size):
                left_key = move(left_key, 4)
                if solve(left_key, lock):
                    return True
            down_key = move(down_key, 1)
            right_key = copy.deepcopy(down_key)
            left_key = copy.deepcopy(down_key)
        for _ in range(size):
            for _ in range(size):
                right_key = move(right_key, 3)
                if solve(right_key, lock):
                    return True
            for _ in range(size):
                left_key = move(left_key, 4)
                if solve(left_key, lock):
                    return True
            up_key = move(up_key, 2)
            right_key = copy.deepcopy(up_key)
            left_key = copy.deepcopy(up_key)
        rotated_key = rotate(rotated_key)
        down_key = copy.deepcopy(rotated_key)
        up_key = copy.deepcopy(rotated_key)

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