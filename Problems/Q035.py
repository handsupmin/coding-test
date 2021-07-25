# Q035.py
# 뱀
from collections import deque

def change_direction(now, command):
    if now == 'right' and command == 'L':
        return 'up'
    elif now == 'right' and command == 'D':
        return 'down'
    elif now == 'left' and command == 'L':
        return 'down'
    elif now == 'left' and command == 'D':
        return 'up'
    elif now == 'up' and command == 'L':
        return 'left'
    elif now == 'up' and command == 'D':
        return 'right'
    elif now == 'down' and command == 'L':
        return 'right'
    elif now == 'down' and command == 'D':
        return 'left'

n = int(input())
k = int(input())
apple = []
for _ in range(k):
    a, b = map(int, input().split())
    apple.append((a, b))

l = int(input())
time_line = []
for _ in range(l):
    a, b = map(str, input().split())
    time_line.append((int(a), b))

time = 0
snake = deque()
snake.append((1, 1))
sequence = 0
direction = 'right'
map_list = [[0] * (n + 1) for _ in range(n + 1)]
for value in apple:
    map_list[value[0]][value[1]] = 1

while True:
    if sequence < l:
        if time_line[sequence][0] == time:
            direction = change_direction(direction, time_line[sequence][1])
            sequence += 1
    
    time += 1

    head = snake[0]
    tail = snake[len(snake)-1]
    
    if direction == 'right':
        dest = (head[0], head[1]+1)
    elif direction == 'left':
        dest = (head[0], head[1]-1)
    elif direction == 'up':
        dest = (head[0]-1, head[1])
    elif direction == 'down':
        dest = (head[0]+1, head[1])

    if dest[0] > n or dest[0] <= 0 or dest[1] > n or dest[1] <= 0:
        print(time)
        break
    elif snake.count(dest) == 1:
        print(time)
        break
    else:
        snake.pop()        
        if map_list[dest[0]][dest[1]] == 1:
            snake.append(tail)
            map_list[dest[0]][dest[1]] = 0
        snake.appendleft(dest)


'''
입력 예시 1
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

출력 예시 1
9

입력 예시 2
10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

출력 예시 2
21

입력 예시 3
10
5
1 5
1 3
1 2
1 6
1 7
4
8 D
10 D
11 D
13 L

출력 예시 3
13
'''