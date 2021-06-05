# Q025.py
"""
모험가 길드
한 마을에 모험가가 N명 있다.
모험가 길드에서 모험가를 대상으로 공포도를 측정했는데,
공포도가 높은 모험가는 쉽게 공포를 느껴 위험 상황에서의 대처 능력이 떨어진다.
모험가 길드는 모험가 그룹을 안전하게 구성하고자 공포도가 X인 모험가는 반드시 X명 이상으로 구성한 모험가 그룹에 참여해야 한다.
이때, 최대 몇개의 모험가 그룹을 만들 수 있는지를 구하라.
1 <= N <= 100000, X <= N (N, X는 자연수)
"""
n = int(input())
person = list(map(int, input().split()))

d = [0] * (n + 1)
for i in person:
    d[i] += 1

count = 0

# 가장 작은 숫자부터 그룹화
for i in range(1, n + 1):
    if d[i] // i > 0:
        count += d[i] // i
        d[i] = d[i] % i
    else: # 이후 남은 인원을 파악하여 그룹화가 가능하면 그룹화
        if sum(d[:i+1]) // i > 0:
            count += sum(d[:i+1]) // i
            d[i] = sum(d[:i+1]) % i

print(count)

"""
입력 예시
5
2 3 1 2 2

출력 예시
2
----------------
입력 예시
11
2 4 1 4 3 1 2 4 5 1 11

출력 예시
5
"""