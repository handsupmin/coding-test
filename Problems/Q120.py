# Q120.py
# https://www.acmicpc.net/problem/1259

while True:
    n = str(input())
    if n == '0':
        break
    if n == n[::-1]:
        print('yes')
    else:
        print('no')