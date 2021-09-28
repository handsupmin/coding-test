# Test.py
# 실험용 파일입니다.

from collections import deque

can_use = []
temp_list = deque()
broken = []

target = input()
num_of_broken = int(input())

if num_of_broken != 0:
    broken = list(map(int,input().split()))

for i in range(10):
    if i not in broken:
        can_use.append(str(i))

if num_of_broken != 10:
    for num in can_use:
        temp_list.append(num)
    
    

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