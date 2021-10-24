# Q202.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-jesse-and-cookies/problem

import heapq

def cookies(k, A):
    # Write your code here
    result = 0
    heapq.heapify(A)
    
    while True:
        first = heapq.heappop(A)
        
        if first >= k:
            return result
        
        if len(A) == 0:
            return -1
        
        second = heapq.heappop(A)
        cookie = first + (2 * second)
        result += 1
        heapq.heappush(A, cookie)

print(cookies(7, [1, 2, 3, 9, 10, 12]))