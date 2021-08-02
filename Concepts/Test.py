# Test.py
# 실험용 파일입니다.

def solution(arr):
    answer = [0, 0]
    n = len(arr)
    half = n // 2
    result = check(arr)
    if sum(result) != 0:
        answer[0] += result[0]
        answer[1] += result[1]
        return answer
    else:
        arr1 = [[-1] * half for _ in range(half)]
        arr2 = [[-1] * half for _ in range(half)]
        arr3 = [[-1] * half for _ in range(half)]
        arr4 = [[-1] * half for _ in range(half)]
        for i in range(n):
            for j in range(n):
                if i < half and j < half:
                    arr1[i][j] = arr[i][j]
                if i < half and j >= half:
                    arr2[i][j-half] = arr[i][j]
                if i >= half and j < half:
                    arr3[i-half][j] = arr[i][j]
                if i >= half and j >= half:
                    arr4[i-half][j-half] = arr[i][j]
        return [solution(arr1)[0] + solution(arr2)[0] + solution(arr3)[0] + solution(arr4)[0], solution(arr1)[1] + solution(arr2)[1] + solution(arr3)[1] + solution(arr4)[1]]
def check(arr):
    if count_arr(arr, 0) == len(arr) * len(arr):
        return [count_arr(arr, 0), 0]
    elif count_arr(arr, 1) == len(arr) * len(arr):
        return [0, count_arr(arr, 1)]
    else:
        return [0, 0]
    
def count_arr(arr, num):
    count = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == num:
                count += 1
    return count