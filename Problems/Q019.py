# Q019.py
"""
효율적인 화폐 구성
N가지 종류의 화폐가 있다. 이 화폐들의 개수를 최소한으로 이용해서 그 가치의 합이 M원이 되도록 하려고 한다.
이때 사용된 최소한의 화폐 개수를 출력한다.
불가능할 때는 -1을 출력한다.
"""
n, m = map(int, input().split())
array = []
for _ in range(n):
    array.append(int(input()))

d = [-1] * 10001

def calc(t):
    tmp = [9999]
    for a in array:
        if d[t-a] != -1:
            tmp.append(d[t-a])
    return min(tmp)

for a in array:
    d[a] = 1

for i in range(1, m+1):
    r = calc(i)
    if r != 9999:
        d[i] = r + 1

print(d[m])

"""
입력
2 15
2
3
출력
5

입력
3 4
3
5
7
출력
-1
"""
