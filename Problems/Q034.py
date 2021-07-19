def solution(key, lock):
    size = len(lock)
    if len(key) < size:
        temp = [[0] * size for _ in range(size)]
        for i in range(key):
            for j in range(key):
                temp[i][j] = key[i][j]
        key = temp
    
    lotated_key = [[0] * size for _ in range(size)]
    moved_key = [[0] * size for _ in range(size)]
    for i in range(size):
        for j in range(size):
            lotated_key[i][j] = key[i][j]
    for _ in range(4):
        lotated_key = rotate(lotated_key)
        for direction in range(1, 5):
            for i in range(size):
                for j in range(size):
                    moved_key[i][j] = lotated_key[i][j]
            for mov in range(len(key)):
                moved_key = move(moved_key, direction)
                count = 0
                for i in range(size):
                    print(moved_key[i], lock[i])
                    for j in range(size):
                        if moved_key[i][j] == 1 and lock[i][j] == 0:
                            count += 1
                print(count)
                if count == size*size:
                    return True
    return False

def rotate(array):
    size = len(array)
    
    result = [[0] * size for x in range(size)]
    
    for i in range(size):
        for j in range(size):
            result[j][size-i-1] = array[i][j]
    return result

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

solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]],	[[1, 1, 1], [1, 1, 0], [1, 0, 1]])