# Q152.py
# https://www.acmicpc.net/problem/2231

n = input()

num = int(n)
length = len(n)
result = 0

for i in range(1, 1000000):
    if i >= num:
        break
    if (sum(list(map(int,str(i)))) + i) == num:
        result = i
        break
    i += 1

print(result)