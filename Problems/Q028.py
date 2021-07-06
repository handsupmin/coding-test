# Q028.py
"""
만들 수 없는 금액
N개의 동전을 이용하여 만들 수 없는 금액의 최솟값을 구하는 프로그램을 작성하라.
"""
n = int(input())
array = list(map(int, input().split()))
array.sort()

target = 1
now = 0

if target == array[now]:
    target += 1
    now += 1



"""
입력 예시
5
3 2 1 1 9
출력 예시
8

입력 예시
3
3 5 7
출력 예시
1
"""