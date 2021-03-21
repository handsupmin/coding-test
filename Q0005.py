# Q0005.py
"""
상하좌우
여행자 A는 N x N 크기의 정사각형 공간 위에 서 있다. 가장 왼쪽 위 좌표는 (1, 1)이고, 가장 오른쪽 아래 좌표는 (N, N)이다.
여행자는 L(왼쪽으로 이동), R(오른쪽으로 이동), U(위로 한 칸 이동), D(아래로 한 칸 이동) 네 가지 패턴으로 움직인다.
공간을 벗어나는 움직임은 무시하며, 여행자가 최종적으로 도착할 지점의 좌표를 출력하라.
"""

n = input()
move = list(map(str, input().split()))

x, y = 1, 1

for i in move:
    if i == 'L':
        if y == 1:
            continue
        y -= 1
    elif i == 'R':
        if y == n:
            continue
        y += 1
    elif i == 'U':
        if x == 1:
            continue
        x -= 1
    elif i == 'D':
        if x == n:
            continue
        x += 1

print(x,y)