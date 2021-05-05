# Q002_math.py

"""
만약 M이 엄청나게 큰 수라면 이전의 방법으로는 시간이 너무 많이 걸리게 된다.
Q002를 수학적 아이디어를 이용하면
K+1 의 몫과 나머지로 문제를 해결할 수 있다.
"""

n, m, k = map(int,input().split())
a = list(map(int,input().split()))

result = 0

a.sort(reverse = True)

first = a[0]
second = a[1]

a1 = m // (k+1) # 몫
a2 = m % (k+1) # 나머지

result = (k * first + second) * a1 + first * a2

print(result)