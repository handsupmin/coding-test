# quickSort.py
# 전통적인 개념의 퀵 정렬
# O(NlogN), 최악의 경우(거의 정렬 된 상태) O(N^2)

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1
        # 만약 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[pivot], array[right] = array[right], array[pivot]
        # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
        else:
            array[right], array[left] = array[left], array[right]
    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)