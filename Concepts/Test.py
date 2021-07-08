# Test.py
# 실험용 파일입니다.

import heapq

q = []
heapq.heappush(q, (0,1))
heapq.heappush(q, (2,3))
heapq.heappush(q, (4,5))

r = heapq.heappop(q)[1]

print(r)