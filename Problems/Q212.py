# Q212.py
# https://www.acmicpc.net/problem/6064

from collections import defaultdict

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    
    if x == y:
        print(x)
        continue

    if m < n:
        m, n = n, m
        x, y = y, x

    num1, num2 = m, n
    d_num1 = defaultdict(int)
    d_num2 = defaultdict(int)

    while num1 != 1:
        for i in range(2, num1 + 1):
            if num1 % i == 0:
                d_num1[i] += 1
                num1 //= i
                break

    while num2 != 1:
        for i in range(2, num2 + 1):
            if num2 % i == 0:
                d_num2[i] += 1
                num2 //= i
                break

    lcm = 1

    for num in d_num1:
        lcm *= (num ** d_num1[num])
    for num in d_num2:
        lcm *= (num ** d_num2[num])
        if num in d_num1:
            lcm //= (num ** min(d_num1[num], d_num2[num]))


    now = y
    result = 0

    while now <= lcm:
        now += n

        if (now % m) == x:
            result = now
            break
        
        if (now % m) == 0 and x == m:
            result = now
            break

    print(result) if result != 0 else print(-1)