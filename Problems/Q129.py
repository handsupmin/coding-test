# Q129.py
# https://www.acmicpc.net/problem/1920

n = int(input())

num_set = set(list(map(int, input().split())))

m = int(input())

for num in list(map(int, input().split())):
    if num in num_set:
        print(1)
    else:
        print(0)