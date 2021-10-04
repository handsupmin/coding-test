# Q106.py
# https://www.acmicpc.net/problem/2562

max_num = 0
max_index = 0
for i in range(1, 10):
    now = int(input())
    if now >= max_num:
        max_num = now
        max_index = i

print(max_num)
print(max_index)