# Q166.py
# https://www.acmicpc.net/problem/1074

n, r, c = map(int, input().split())

result = 0

while n != 1:
    if 0 <= r <= (2 ** (n - 1) - 1):
        position = [0, 1]
    elif (2 ** (n - 1)) <= r <= (2 ** n - 1):
        position = [2, 3]
        r -= (2 ** (n - 1))
    if 0 <= c <= (2 ** (n - 1) - 1):
        position = position[0]
    elif (2 ** (n - 1)) <= c <= (2 ** n - 1):
        position = position[1]
        c -= (2 ** (n - 1))
    result += (2 ** (2 * n - 2) * position)
    n -= 1

if n == 1:
    if r == 0:
        position = [0, 1]
    elif r == 1:
        position = [2, 3]
    if c == 0:
        position = position[0]
    elif c == 1:
        position = position[1]
    result += position

print(result)