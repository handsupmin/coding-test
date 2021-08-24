# Q058.py
# https://www.acmicpc.net/problem/18428

from itertools import combinations

def check(array, x, y):
    n = len(array)
    for i in range(x):
        if array[x-i-1][y] == 1:
            return False
        elif array[x-i-1][y] == 2 or array[x-i-1][y] == 3:
            break

    for i in range(x+1,n):
        if array[i][y] == 1:
            return False
        elif array[i][y] == 2 or array[i][y] == 3:
            break

    for i in range(y):
        if array[x][y-i-1] == 1:
            return False
        elif array[x][y-i-1] == 2 or array[x][y-i-1] == 3:
            break

    for i in range(y+1,n):
        if array[x][i] == 1:
            return False
        elif array[x][i] == 2 or array[x][i] == 3:
            break

    return True

n = int(input())

array = []
for _ in range(n):
    array.append(list(map(str, input().split())))

obj = []
t_list = []
for i in range(n):
    for j in range(n):
        if array[i][j] == 'X':
            array[i][j] = 0
            obj.append((i, j))
        elif array[i][j] == 'S':
            array[i][j] = 1
        elif array[i][j] == 'T':
            array[i][j] = 2
            t_list.append((i, j))


obj_list = list(combinations(obj, 3))
yes_or_no = 0

for value in obj_list:
    for i in value:
        array[i[0]][i[1]] = 3
    count = 0
    for t in t_list:
        if check(array, t[0], t[1]) == True:
            count += 1
    yes_or_no = max(yes_or_no, count)
    for i in value:
        array[i[0]][i[1]] = 0

if yes_or_no == len(t_list):
    print("YES")
else:
    print("NO")