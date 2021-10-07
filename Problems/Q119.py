# Q119.py
# https://www.acmicpc.net/problem/1181

import sys
input = sys.stdin.readline

n = int(input().rstrip())
words = set()

for _ in range(n):
    words.add(input().rstrip())

words = list(words)
words.sort()
words.sort(key = lambda x : len(x))

for w in words:
    print(w)