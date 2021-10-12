# Q146.py
# https://www.acmicpc.net/problem/10816

from collections import defaultdict

n = int(input())
deck = defaultdict(int)

for num in list(map(int, input().split())):
    deck[num] += 1

m = int(input())
result = []
for num in list(map(int, input().split())):
    if num in deck:
        result.append(deck[num])
    else:
        result.append(0)

for i in range(len(result)):
    print(result[i])