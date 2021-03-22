# Q007.py
"""
체스판에서 나이트가 이동할 수 있는 경우의 수를 계산하여 출력
  a b c d e f g h
1
2
3
4
5
6
7
8
와 같은 형식으로 이루어진 체스판에서 지정한 위치에서 나이트가 체스판을 벗어나지 않고 움직일 수 있는 경우의 수를 구하라.
"""

start = input()

x = start[1]
y = start[0]
count = 0

y_index = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
for i in y_index:
    if y == i:
        y = y_index.index(i) + 1

move = [[-2,-1], [-2, 1], [-1, -2], [-1, 2], [1, 2], [1, -2], [2, 1], [2, -1]]

for j in move:
    j[0] = int(x) + j[0]
    j[1] = int(y) + j[1]
    if 0 < j[0] < 9 and 0 < j[1] < 9:
        count += 1

print(count)
