# Q094.py
# https://www.acmicpc.net/problem/5430

from collections import deque

t = int(input())

for _ in range(t):
    result = ''
    r_count = 0
    commands = list(map(str, input()))
    array_number = int(input())
    if array_number == 0:
        temp = input()
        array = []
    elif array_number == 1:
        array = [input()[1:-1]]
    else:
        array = list(map(str, input()[1:-1].split(',')))
    array = deque(array)
    for command in commands:
        if result == 'error':
            break
        if command == 'R':
            r_count += 1
        if command == 'D':
            if array_number <= 0:
                result = 'error'
                break
            elif array_number == 1:
                array = []
                array_number -= 1
            else:
                if r_count % 2 == 0:
                    array.popleft()
                else:
                    array.pop()
                array_number -= 1
    array = list(array)
    if r_count % 2 == 1:
        array = array[::-1]
    if result != 'error':
        result = '[' + ','.join(array) + ']'
    print(result)