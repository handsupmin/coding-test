# Q128.py
# https://www.acmicpc.net/problem/1874

n = int(input())

stack = []
target = []
now = 1
idx = 0

result = []

for _ in range(n):
    target.append(int(input()))

while idx != n:
    if now > n:
        break
    stack.append(now)
    result.append('+')
    while True:
        if len(stack) != 0 and stack[len(stack) - 1] == target[idx]:
            stack.pop()
            result.append('-')
            idx += 1
        else:
            break
    now += 1

if result.count('-') != n:
    print("NO")
else:
    for op in result:
        print(op)