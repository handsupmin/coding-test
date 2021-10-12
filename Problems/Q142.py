# Q142.py
# https://www.acmicpc.net/problem/4153

while True:
    data = list(map(int,input().split()))
    if sum(data) == 0:
        break
    data.sort()
    a, b, c = data
    if c ** 2 == a ** 2 + b ** 2:
        print("right")
    else:
        print("wrong")