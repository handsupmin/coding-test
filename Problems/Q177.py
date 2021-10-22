# Q177.py
# https://www.acmicpc.net/problem/2630

import sys
input = sys.stdin.readline

def count_paper(x, y, length):
    if length == 1:
        return (1, 0) if big_paper[x][y] == 1 else (0, 1)

    num_blue = 0
    num_white = 0
    for i in range(x, x + length):
        for j in range(y, y + length):
            if big_paper[i][j] == 1:
                num_blue += 1 
            else:
                num_white += 1
    if num_blue == length ** 2:
        return (1, 0)
    elif num_white == length ** 2:
        return (0, 1)
    else:
        length //= 2
        result1 = count_paper(x, y, length)
        result2 = count_paper(x + length, y, length)
        result3 = count_paper(x, y + length, length)
        result4 = count_paper(x + length, y + length, length)
        return (result1[0] + result2[0] + result3[0] + result4[0], result1[1] + result2[1] + result3[1] + result4[1])

n = int(input())

big_paper = []

for _ in range(n):
    big_paper.append(list(map(int, input().split())))

result = count_paper(0, 0, n)

print(result[1])
print(result[0])