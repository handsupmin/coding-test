# Q011.py
# 위애서 아래로
"""
위에서 아래로
첫째 줄에 수열에 속해 있는 수의 개수 N이 주어진다.
둘째 줄부터 N+1번째 줄까지 N개의 수가 입력된다.
입력으로 주어진 수열이 내림차순으로 정렬된 결과를 공백으로 구분하여 출력한다.
"""

n = input()
result = []

for _ in range(int(n)):
    result.append(input())

result.sort()
result.reverse()

for x in result:
    print(x, end = " ")

"""
3
15
27
12
"""