# Q108.py
# https://www.acmicpc.net/problem/2675

t = int(input())

for _ in range(t):
    r, s = input().split()
    r = int(r)
    result = ''

    for i in range(len(s)):
        result += s[i] * r

    print(result)