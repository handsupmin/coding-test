# Q015.py
# 떡볶이 떡 만들기
"""
파라메트릭 서치
"""

n, m = map(int, input().split())
a = list(map(int, input().split()))

a.sort(reverse = True)
i = a[1]
result = 0
while True:
    for j in a:
        if j <= i:
            break
        result += (j - i)
    if result >= m:
        break
    else:
        result = 0
        i -= 1

print(i)

"""
입력 예시
10 16
19 15 10 17 18 12 17 12 15 14

출력 예시
14
"""
