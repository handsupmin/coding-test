# Q092.py
# https://www.acmicpc.net/problem/1107

from collections import deque

def _in_range(num):
    if num < 0:
        return num + 10
    elif num > 9:
        return num - 10
    else:
        return num

can_use = [0] * 10
mini = 100
candidate = [100]
temp_list = deque()

target = input()
num_of_broken = int(input())

if num_of_broken != 0:
    for button in list(map(int,input().split())):
        can_use[button] = 1

if num_of_broken != 10:
    for i in range(10):
        if can_use[i] == 0:
            mini = i
            break

    for i in range(len(target)):
        now = target[i]
        if can_use[int(now)] == 0:
            if len(temp_list) == 0:
                temp_list.append(now)
            else:
                n = len(temp_list)
                for _ in range(n):
                    value = temp_list.popleft()
                    temp_list.append(value + now)
                    temp_list.append(now)
        else:
            num_left = _in_range(int(now) - 1)
            num_right = _in_range(int(now) + 1)
            while can_use[num_left] != 0:
                num_left = _in_range(num_left - 1)
            while can_use[num_right] != 0:
                num_right = _in_range(num_right + 1)

            if len(temp_list) == 0:
                temp_list.append(str(num_left))
                temp_list.append(str(num_right))
            else:
                n = len(temp_list)
                for _ in range(n):
                    value = temp_list.popleft()
                    temp_list.append(value + str(num_left))
                    temp_list.append(value + str(num_right))
                    temp_list.append(str(num_left))
                    temp_list.append(str(num_right))


temp_list.append('100')

temp_list = list(map(int, temp_list))
temp_list = set(temp_list)
temp_list = list(temp_list)
            
for i in range(len(temp_list)):
    if mini == 100:
        break
    if len(str(temp_list[i])) == len(target):
        temp_list.append(int(str(temp_list[i]) + str(mini)))

print(temp_list)
        
result_list = []
for value in temp_list:
    result_list.append(abs(int(target) - value) + len(str(value)))
    result_list.append(abs(int(target) - 100))

print(min(result_list))