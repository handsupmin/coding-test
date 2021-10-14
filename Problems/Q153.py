# Q153.py
# https://www.acmicpc.net/problem/2292

n = int(input())

bound = 1
count = 1
while bound < n:
    bound += count * 6
    count += 1

print(count)