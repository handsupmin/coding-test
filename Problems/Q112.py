# Q112.py
# https://www.acmicpc.net/problem/8958

n = int(input())

for _ in range(n):
    now = 0
    oxs = list(map(str, input()))
    result = 0
    for i in range(len(oxs)):
        if oxs[i] == 'O':
            now += 1
            result += now
        else:
            now = 0
    print(result)