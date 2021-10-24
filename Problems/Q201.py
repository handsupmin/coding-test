# Q201.py
# https://www.acmicpc.net/problem/1780

import sys
input = sys.stdin.readline

def count_paper(x, y, length):
    if length == 1:
        if big_paper[x][y] == -1:
            return (1, 0, 0)
        elif big_paper[x][y] == 0:
            return (0, 1, 0)
        else:
            return (0, 0, 1)

    count_plus = 0
    count_minus = 0
    count_zero = 0
    for i in range(x, x + length):
        for j in range(y, y + length):
            if big_paper[i][j] == 1:
                count_plus += 1
            elif big_paper[i][j] == -1:
                count_minus += 1
            else:
                count_zero += 1
    
    if count_minus == (length ** 2):
        return (1, 0, 0)
    elif count_zero == (length ** 2):
        return (0, 1, 0)
    elif count_plus == (length ** 2):
        return (0, 0, 1)
    elif length == 3:
        return (count_minus, count_zero, count_plus)
    else:
        length //= 3
        results = []
        
        results.append(count_paper(x, y, length))
        results.append(count_paper(x, y + length, length))
        results.append(count_paper(x, y + (length * 2), length))
        results.append(count_paper(x + length, y, length))
        results.append(count_paper(x + length, y + length, length))
        results.append(count_paper(x + length, y + (length * 2), length))
        results.append(count_paper(x + (length * 2), y, length))
        results.append(count_paper(x + (length * 2), y + length, length))
        results.append(count_paper(x + (length * 2), y + (length * 2), length))
        
        result_minus = 0
        result_zero = 0
        result_plus = 0

        for minus, zero, plus in results:
            result_minus += minus
            result_zero += zero
            result_plus += plus

        return (result_minus, result_zero, result_plus)

n = int(input())

big_paper = []

for _ in range(n):
    big_paper.append(list(map(int, input().split())))

result = count_paper(0, 0, n)

print(result[0])
print(result[1])
print(result[2])