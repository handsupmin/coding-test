import heapq

def solution(food_times, k):
    answer = 0
    q = []
    num = 0
    k += 1
    n1 = 0
    n2 = 0
    for value in food_times:
        num += 1
        heapq.heappush(q, (value, num))
    
    n1 = heapq.heappop(q)[0]
    k -= n1 * num
    num -= 1
    while True:
        if num < 0:
            return -1
        if k <= num:
            break
        n2 = n1
        n1 = heapq.heappop(q)[0]
        k -= (n1 - n2) * num
        num -= 1
    
    for _ in range(k):
        answer = heapq.heappop(q)[1]
    
    return answer