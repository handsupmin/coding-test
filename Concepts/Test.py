# Test.py
# 실험용 파일입니다.

import heapq

string = input()
alpha = []

for i in string:
    heapq.heappush(alpha, i)

while alpha:
    print(heapq.heappop(alpha))