# Q022.py
# 팀 결성
"""
힉교에서 학생들에게 0번부터 N번까지의 번호를 부여했다.
처음에는 모든 학생이 서로 다른 팀으로 구분되어, 총 N + 1갸의 팀이 존재한다.
이때 선생님은 '팀 합치기' 연산과 '같은 팀 여부 확인' 연산을 사용할 수 있다.
선생님이 M개의 연산을 수행할 수 있을 때, '같은 팀 여부 확인' 연산에 대한 연산 결과를 출력하는 프로그램을 작성하시오.
'팀 합치기' 연산은 0 a b 형태로 주어진다. 이는 a번 학생이 속한 팀과 b번 학생이 속한 팀을 합친다는 의미이다.
'같은 팀 여부 확인' 연산은 1 a b 형태로 주어진다. 이는 a번 학생과 b번 학생이 같은 팀에 속해 있는지를 확인하는 연산이다
'같은 팀 여부 확인' 연산에 대하여 한 줄에 하나씩 YES 혹은 NO로 결과를 출력한다.
"""
n, m = map(int, input().split())

team = [0] * (n + 1)
array = []

def find_team(team, a):
    if team[a] != a:
        team[a] = find_team(team, team[a])
    return team[a]

def union_team(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a < b:
        team[b] = a
    else:
        team[a] = b

def is_sameteam(team, a, b):
    a = find_team(team, a)
    b = find_team(team, b)
    if a == b:
        print("YES")
    else:
        print("NO")

for i in range(0, n + 1):
    team[i] = i

for _ in range(m):
    prm, n1, n2 = map(int, input().split())
    array.append((prm, n1, n2))

for i in array:
    prm, n1, n2 = i
    if prm == 0:
        union_team(team, n1, n2)
    elif prm == 1:
        is_sameteam(team, n1, n2)

"""
입력 예시
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력 예시
NO
NO
YES
"""