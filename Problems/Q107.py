# Q107.py
# https://www.acmicpc.net/problem/2577

count = [0] * 10

a = int(input())
b = int(input())
c = int(input())

multiple = str(a * b * c)

for i in range(len(multiple)):
    count[int(multiple[i])] += 1

for num in count:
    print(num)