# Q131.py
# https://www.acmicpc.net/problem/1966

from collections import deque

num_of_case = int(input())

for _ in range(num_of_case):
    num_of_document, target_index = map(int, input().split())
    documents = deque()
    count = 0
    priorities = list(map(int, input().split()))
    for idx, priority in enumerate(priorities):
        documents.append((idx, priority))
    priorities.sort(reverse = True)
    priorities = deque(priorities)

    while documents:
        index, priority = documents.popleft()
        if priority == priorities[0]:
            count += 1
            priorities.popleft()
            if index == target_index:
                print(count)
                break
        else:
            documents.append((index, priority))