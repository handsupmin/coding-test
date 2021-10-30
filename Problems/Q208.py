# Q208.py
# https://www.acmicpc.net/problem/9461

for _ in range(int(input())):
    n = int(input())

    d = [0] * n
    
    if n <= 3:
        print(1)
    elif n <= 4:
        print(2)
    else:
        d[0] = 1
        d[1] = 1
        d[2] = 1
        d[3] = 2
        d[4] = 2

        for i in range(5, n):
            d[i] = d[i-1] + d[i-5]
        
        print(d[n-1])