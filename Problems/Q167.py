# Q167.py
# https://www.acmicpc.net/problem/1620

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
poke = dict()
index = dict()
numbers = set(map(str, range(0, 10)))

for i in range(1, n + 1):
    pokemon = input().rstrip()
    poke[str(i)] = pokemon
    index[pokemon] = i

for _ in range(m):
    question = input().rstrip()
    if question[0] in numbers:
        print(poke[question])
    else:
        print(index[question])