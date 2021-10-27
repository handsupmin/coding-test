# Q205.py
# https://www.acmicpc.net/problem/11047

n, k = map(int, input().split())
coins = []

for _ in range(n):
    coin = int(input())
    if coin > k:
        continue
    coins.append(coin)

coins.sort(reverse = True)
result = 0

for coin in coins:
    result += k // coin
    k %= coin

print(result)