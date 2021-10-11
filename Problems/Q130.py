# Q130.py
# https://www.acmicpc.net/problem/1929

n=1000000
a = [False,False] + [True]*(n-1)

start, end = map(int, input().split())

for prime in range(2,n+1):
    if prime <= end:
        if a[prime]:
            if start <= prime <= end:
                print(prime)
            for j in range(2*prime, n+1, prime):
                a[j] = False
    else:
        break