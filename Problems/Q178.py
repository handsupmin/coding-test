# Q178.py
# https://www.acmicpc.net/problem/9095

def count_method(n):
    if n < 0:
        return 0
    if n == 0:
        return 1
    return count_method(n-1) + count_method(n-2) + count_method(n-3)

t = int(input())

for _ in range(t):
    n = int(input())
    print(count_method(n))
