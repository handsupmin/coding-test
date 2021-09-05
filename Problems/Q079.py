# Q079.py
# 1로 만들기

n = int(input())

d = [0] * (n+1)

d[1] = 1
d[2] = 1
d[3] = 1
d[5] = 1

for i in range(3, n+1):
    if d[i] == 0:
        d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i // 2] + 1, d[i])
    if i % 3 == 0:
        d[i] = min(d[i // 3] + 1, d[i])
    if i % 5 == 0:
        d[i] = min(d[i // 5] + 1, d[i])

print(d[n])