# BinarySearch.py

# 이진탐색 재귀함수
def binary_search(array, target, start, end):    
    mid = (start + end) // 2
    if start > end:
        return -1
    if target == array[mid]:
        return mid
    elif array[start] < target < array[mid]:
        return binary_search(array, target, start, mid-1)
    else:
        return binary_search(array, target, mid+1, end)

# 이진탐색 반복함수
def binary_search2(array, target, start, end):
    while(start <= end):
        mid = (start + end) // 2
        if target == array[mid]:
            return mid
        elif array[start] < target < array[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


n, t = map(int, input().split())
array = list(map(int, input().split()))

index = binary_search(array, t, 0, len(array)-1)

if index == -1:
    print("원소가 존재하지 않습니다.")
else:
    print(index + 1, "번째에 원소가 있습니다")

index2 = binary_search2(array, t, 0, len(array)-1)

if index2 == -1:
    print("원소가 존재하지 않습니다.")
else:
    print(index2 + 1, "번째에 원소가 있습니다")

"""
10 9
1 3 5 7 9 11 13 15 17 19

10 8
1 3 5 7 9 11 13 15 17 19
"""

