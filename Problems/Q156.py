# Q156.py
# https://www.acmicpc.net/problem/4949

while True:
    value = input()
    if value == '.':
        break
    small = 0
    big = 0

    for word in list(value):
        if word == '(':
            small += 1
        elif word == ')' and small != 0:
            small -= 1
        elif word == ')' and small == 0:
            small = 1
            break
        elif word == '[':
            big += 1
        elif word == ']' and big != 0:
            big -= 1
        elif word == ']' and big == 0:
            big = 1
            break
    if not small and not big:
        print('yes')
    else:
        print('no')