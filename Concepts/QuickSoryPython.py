# quickSoryPython.py
# 파이썬의 장점을 살린 퀵 정렬
# 전통적인 방법의 코드보다 시간 면에서는 조금 비효율적이다.

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array

    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

print(quick_sort(array))