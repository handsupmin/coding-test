# Q092.py
# https://www.acmicpc.net/problem/1107

from collections import deque

can_use = []
temp_list = []
broken = []

target = input()
num_of_broken = int(input())

if num_of_broken != 0:
    broken = list(map(int,input().split()))

for i in range(10):
    if i not in broken:
        can_use.append(str(i))

if num_of_broken != 10:
    temp = []
    for num in can_use:
        temp.append(num)
    temp2 = []
    for num in can_use:
        for value in temp:
            temp2.append(value + num)
    temp3 = []
    for num in can_use:
        for value in temp2:
            temp3.append(value + num)
    temp4 = []
    for num in can_use:
        for value in temp3:
            temp4.append(value + num)
    temp5 = []
    for num in can_use:
        for value in temp4:
            temp5.append(value + num)
    temp6 = []
    for num in can_use:
        for value in temp5:
            temp6.append(value + num)
    
    temp_list += temp + temp2 + temp3 + temp4 + temp5 + temp6

temp_list = list(map(int, temp_list))

result_list = []
for value in temp_list:
    result_list.append(abs(int(target) - value) + len(str(value)))
result_list.append(abs(int(target) - 100))

print(min(result_list))