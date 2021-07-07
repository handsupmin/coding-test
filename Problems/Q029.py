# Q029.py
"""
볼링공 고르기
1~M까지의 무게를 가진 볼링공 중, 서로 다른 무게의 볼링공을 고르는 모든 경우의 수를 구하라.
"""
n, m = map(int, input().split())
array = list(map(int, input().split()))
count = 0

for i in range(n):
    for j in range(i+1, n):
        if array[i] != array[j]:
            count += 1

print(count)
"""
입력 예시
5 3
1 3 2 3 2
출력 예시
8

입력 예시
8 5
1 5 4 3 2 4 5 2
출력 예시
25
"""