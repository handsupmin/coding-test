# Q105.py
# https://www.acmicpc.net/problem/2475

data = list(map(int, input().split()))

for i in range(len(data)):
    data[i] *= data[i]

print(sum(data)%10)