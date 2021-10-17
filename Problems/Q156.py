# Q156.py
# https://www.acmicpc.net/problem/4949

while True:
    value = input()
    if value == '.':
        break
    stack = []
    is_ok = True
    for i in range(len(value) - 1):        
        if value[i] == '(':
            stack.append('(')
        elif value[i] == '[':
            stack.append('[')
        elif value[i] == ')' and len(stack) == 0:
            is_ok = False
            break
        elif value[i] == ')' and stack[len(stack) - 1] != '(':
            is_ok = False
            break
        elif value[i] == ')' and stack[len(stack) - 1] == '(':
            stack.pop()
        if value[i] == ']' and len(stack) == 0:
            is_ok = False
            break
        elif value[i] == ']' and stack[len(stack) - 1] != '[':
            is_ok = False
            break
        elif value[i] == ']' and stack[len(stack) - 1] == '[':
            stack.pop()
    if is_ok and not len(stack):
        print('yes')
    else:
        print('no')