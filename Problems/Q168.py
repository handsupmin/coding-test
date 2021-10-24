# Q168.py
# https://www.acmicpc.net/problem/7662

import heapq
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    k = int(input())
    minq = []
    maxq = []
    visited = [False] * (k)
    for i in range(k):
        query, number = input().split()
        number = int(number)
        if query == 'I':
            heapq.heappush(minq, (number, i))
            heapq.heappush(maxq, (-number, i))
            visited[i] = True

        elif number == -1:
            while minq and not visited[minq[0][1]]:
                heapq.heappop(minq)
            if minq:
                visited[minq[0][1]] = False
                heapq.heappop(minq)

        elif number == 1:
            while maxq and not visited[maxq[0][1]]:
                heapq.heappop(maxq)
            if maxq:
                visited[maxq[0][1]] = False
                heapq.heappop(maxq)

    while minq and not visited[minq[0][1]]:
        heapq.heappop(minq)
    while maxq and not visited[maxq[0][1]]:
        heapq.heappop(maxq)

    print(f'{-maxq[0][0]} {minq[0][0]}' if maxq and minq else 'EMPTY')