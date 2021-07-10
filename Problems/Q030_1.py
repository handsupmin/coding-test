# Q030_1.py
import heapq

def solution(food_times, k):
    answer = 0
    q = []
    num = 0
    n1 = 0
    for value in food_times:
        num += 1
        heapq.heappush(q, (value, num))
    
    temp = heapq.heappop(q)
    n1 = temp[0]
    k -= n1 * num
    print(q, k)
    while True:
        num -= 1
        if num < 0:
            return -1
        if k <= 0:
            heapq.heappush(q, temp)
            num += 1
            k += n1 * num
            break
        temp = heapq.heappop(q)
        n1 = temp[0] - n1
        k -= n1 * num
        print(q, k)
    
    h = []
    for a in q:
        heapq.heappush(h, (a[1], a[0]))
    
    for _ in range(k%num):
        answer = heapq.heappop(h)[0]
    
    return answer