# Q161.py
# https://www.acmicpc.net/problem/11651

n = int(input())

array = []

for _ in range(n):
    array.append(list(map(int, input().split())))

array.sort(key = lambda x : (x[1], x[0]))
for x, y in array:
    print(x, y)