# Q199.py
# https://www.acmicpc.net/problem/1541

value = input()

value = value.split('-')

if len(value) == 1:
    result = sum(list(map(int, value[0].split('+'))))
else:
    result = sum(list(map(int, value[0].split('+'))))
    for i in range(1, len(value)):
        result -= sum(list(map(int, value[i].split('+'))))

print(result)