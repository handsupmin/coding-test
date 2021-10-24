# Q165.py
# https://www.acmicpc.net/problem/1463

n = int(input())
d = [0] * (n + 1)

if n == 1:
    print(0)
elif n == 2:
    print(1)
elif n >= 3:    
    d[3] = 1
    d[2] = 1
    for i in range(4, n + 1):
        if i % 2 == 0 and i % 3 == 0:
            d[i] = min(d[i-1] + 1, d[i//2] + 1, d[i//3] + 1)
        elif i % 2 == 0:
            d[i] = min(d[i-1] + 1, d[i//2] + 1)
        elif i % 3 == 0:
            d[i] = min(d[i-1] + 1, d[i//3] + 1)
        else:
            d[i] = d[i-1] + 1

    print(d[n])