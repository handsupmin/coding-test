# Q200.py
# https://www.acmicpc.net/problem/1676

n = int(input())

num_of_five = 0

for i in range(1, n + 1):
    if i % 5 == 0:
        t = i
        while t % 5 == 0 and t // 5 != 0:
            t //= 5
            num_of_five += 1

print(num_of_five)