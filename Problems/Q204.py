# Q204.py
# https://www.acmicpc.net/problem/1992

def make_quad(x, y, length):
    if length == 1:
        return str(array[x][y])
    count_one = 0
    count_zero = 0

    for i in range(x, x + length):
        for j in range(y, y + length):
            if array[i][j] == 1:
                count_one += 1

            else:
                count_zero += 1

            if count_one and count_zero:
                break

        if count_one and count_zero:
            bound = length // 2
            result1 = make_quad(x, y, bound)
            result2 = make_quad(x, y + bound, bound)
            result3 = make_quad(x + bound, y, bound)
            result4 = make_quad(x + bound, y + bound, bound)
            return '(' + result1 + result2 + result3 + result4 + ')'

    return '1' if count_one else '0'

n = int(input())
array = []

for _ in range(n):
    array.append(list(map(int,input())))

print(make_quad(0, 0, n))