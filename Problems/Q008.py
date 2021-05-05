# Q008.py
"""
게임 개발
게임 캐릭터가 움직이는 시스템을 개발한다. 캐릭터는 동서남북중 한 곳을 바라본다.
맵의 시작은 0x0이고, 맵의 크기는 N x M 크기의 직사각형이다. 각 칸은 1(바다), 혹은 0(육지)로 이루어져있다.
맵은 (A, B) 형태의 좌표로 나타나고 A는 북쪽으로부터 떨어진 개수, B는 서쪽으로부터 떨어진 개수이다.
캐릭터는 상하좌우로 움질일 수 있고, 바다로 되어 있는 공간에는 갈 수 없다.
캐릭터는 현재 위치에서 현재 방향을 기준으로 왼쪽 방향부터 갈 곳을 정한다.
캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다. 왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽 방향으로 회전만 수행하고 1단계로 돌아간다.
만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고 1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
이러한 메뉴얼로 이동한 캐릭터가 방문한 칸의 수를 출력하라.
"""

n, m = map(int, input().split())

x, y, direction = map(int, input().split())

teritory = []
for _ in range(n):
    teritory.append(list(map(int, input().split())))

count = 0
breakpoint = 0

while breakpoint != 1:
    if (teritory[x][y-1] == 3 or teritory[x][y-1] == 1) and (teritory[x+1][y] == 3 or teritory[x+1][y] == 1) and (teritory[x][y+1] == 3 or teritory[x][y+1] == 1) and (teritory[x-1][y] == 3 or teritory[x-1][y] == 1):
        if direction == 0:
            x += 1
        elif direction == 3:
            y += 1
        elif direction == 2:
            x -= 1
        elif direction == 1:
            y -= 1
        if teritory[x][y] == 1:
            for i in range(n):
                for j in range(m):
                    if teritory[i][j] == 3:
                        count += 1
            print(count)
            breakpoint = 1
    elif direction == 0 and teritory[x][y-1] == 0:
        direction = 3
        y = y-1
        teritory[x][y] = 3
    elif direction == 0 and teritory[x][y-1] != 0:
        direction = 3
    elif direction == 3 and teritory[x+1][y] == 0:
        direction = 2
        x = x+1
        teritory[x][y] = 3
    elif direction == 3 and teritory[x+1][y] != 0:
        direction = 2
    elif direction == 2 and teritory[x][y+1] == 0:
        direction = 1
        y = y+1
        teritory[x][y] = 3
    elif direction == 2 and teritory[x][y+1] != 0:
        direction = 1
    elif direction == 1 and teritory[x-1][y] == 0:
        direction = 0
        x = x-1
        teritory[x][y] = 3
    elif direction == 1 and teritory[x-1][y] != 0:
        direction = 0
    

"""
5 5
1 1 0
1 1 1 1 1
1 0 0 0 1
1 1 0 0 1
1 1 1 0 1
1 1 1 1 1
"""