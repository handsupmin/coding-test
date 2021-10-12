# Q145.py
# https://www.acmicpc.net/problem/10814

import sys
input = sys.stdin.readline

member = []

n = int(input())

for i in range(n):
    age, name = list(input().split())
    member.append((int(age), i, name))

member.sort(key = lambda x : (x[0], x[1]))

for i in range(n):
    print(member[i][0], member[i][2])