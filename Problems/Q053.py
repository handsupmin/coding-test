# Q053.py
# 연산자 끼워넣기

from itertools import permutations

oper = []
n = int(input())
number = list(map(int,input().split()))

t = list(map(int,input().split()))

oper += t[0] * '+'
oper += t[1] * '-'
oper += t[2] * '*'
oper += t[3] * '/'

permu = list(permutations(oper, len(oper)))

result = []
for value in permu:
    num = number[0]
    for i in range(len(value)):
        if value[i] == '+':
            num += number[i+1]
        elif value[i] == '-':
            num -= number[i+1]
        elif value[i] == '*':
            num *= number[i+1]
        else:
            if num < 0:
                num = -num
                num //= number[i+1]
                num = -num
            else:
                num //= number[i+1]
    result.append(num)

print(max(result))
print(min(result))