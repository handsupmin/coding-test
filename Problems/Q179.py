# Q179.py
# https://www.acmicpc.net/problem/11399

n = int(input())
times = list(map(int, input().split()))

times.sort()
result = 0

for time in times:
    result += time * n
    n -= 1

print(result)