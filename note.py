# note.py
# 여러가지를 연습해보기 위한 연습장입니다.

"""
# 파이썬에서 많은 양의 입력을 받을 때 사용하는 sys.stdin.readline() 함수
# input()은 동작 속도가 느리다.
import sys
# readline시 엔터가 줄바꿈 기호(\n)로 입력되는데, 이를 지우기 위하여 rstrip() 사용

for i in range(10):
    data = sys.stdin.readline().rstrip()

print(data)


# f-string

answer = 7
print(f"정답은 {answer}입니다.")

# itertools, 순열, 조합
from itertools import permutations

data = ['A', 'B', 'C']

result = list(permutations(data, 3)) # 모든 순열 구하기

print(result)
"""

# 재귀함수를 이용한 팩토리얼

def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))