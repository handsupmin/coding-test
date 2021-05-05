# heapq.py
import heapq
from copy import copy # 객체 복사를 위한 함수

# 파이썬은 min heap을 지원
def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽인
    for value in iterable:
        heapq.heappush(h, value)
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

# Max heap을 구현하려면 부호를 바꿔주면 된다.
def heapsort2(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽인
    for value in iterable:
        heapq.heappush(h, -value) # 삽입 시 부호를 바꿔준 후
    # 힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(-heapq.heappop(h)) # 원소를 꺼낼 때 다시 부호를 바꾸어 준다.
    return result

a = ([1, 3, 5, 7, 9, 2, 4, 6, 8, 0])
b = copy(a)
# copy 없이 b = a[:]로도 사용 가능
result = heapsort(a)
result2 = heapsort2(b)

print(result)
print(result2)