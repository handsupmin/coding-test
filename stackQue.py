# stackQue.py

# stack

stack = []

stack.append(5)
stack.append(1)
stack.append(2)
stack.append(3)
stack.pop()
stack.append(6)
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력
# arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라

# queue

from collections import deque

queue = deque()

queue.append(5)
queue.append(1)
queue.append(2)
queue.append(3)
queue.popleft()
queue.append(6)
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) # 먼저 들어온 원소부터 출력    
queue.reverse() # 큐를 역순으로 바꾸기
print(queue) # 나중에 들어온 원소부터 출력