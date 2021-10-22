# Q175.py
# https://www.acmicpc.net/problem/18870

n = int(input())
num_dict = dict()
target = list(map(int, input().split()))

num_set = set(target)
num_list = list(num_set)
num_list.sort()

for idx in range(len(num_list)):
    num_dict[num_list[idx]] = idx

for num in target:
    print(num_dict[num], end = ' ')