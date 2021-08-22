# Q051_math.py
# 경쟁적 감염
# https://www.acmicpc.net/problem/18405
# 수학적 풀이

def calc(virus, s):
    for time in range(1, s+1):
        for i in range(len(virus)):
            for v in virus[i]:
                if v <= time:
                    return i
    return 0

n, k = map(int, input().split())
array = []
virus = [[] for _ in range(k+1)]

for _ in range(n):
    array.append(list(map(int, input().split())))

s, x, y = map(int, input().split())

for i in range(1, k+1):
    for a in range(n):
        for b in range(n):
            if array[a][b] == i:
                virus[i].append(abs(a-(x-1)) + abs(b-(y-1)))

print(calc(virus, s))

"""
예제 입력 1
3 3
1 0 2
0 0 0
3 0 0
2 3 2

예제 출력 1 
3

예제 입력 2 
3 3
1 0 2
0 0 0
3 0 0
1 2 2

예제 출력 2 
0
"""