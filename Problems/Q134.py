# Q134.py
# https://www.acmicpc.net/problem/2164

from collections import deque

n = int(input())

deck = list(range(1, n + 1))
deck = deque(deck)

while len(deck) != 1:
    deck.popleft()
    if len(deck) == 1:
        break
    deck.append(deck.popleft())

print(deck[0])