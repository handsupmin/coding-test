# Q080.py
# 효율적인 화폐 구성

n, m = map(int, input().split())
d = [-1] * (10000)

coins = set()
for _ in range(n):
    coin = int(input())
    d[coin] = 1
    coins.add(coin)

for i in range(min(coins), m+1):
    if d[i] == -1:
        case = set()
        for coin in coins:
            if d[i - coin] != -1:
                case.add(d[i - coin] + 1)
        if len(case) != 0:
            d[i] = min(case)

print(d[m])