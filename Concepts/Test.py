# Test.py
# 실험용 파일입니다.

from collections import deque

c = deque()
c.append((1, 1))
c.append((2, 2))
c.append((3, 3))

print(c.count((1,1)))