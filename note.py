# note.py
# 여러가지를 연습해보기 위한 연습장입니다.


# 문자 입력 받기
n, m, k = map(int,input().split())
a = list(map(int,input().split()))

# 문자 뒤에 공백 삽입
for v in range(3):
    print(v, end=' ')

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


# 재귀함수를 이용한 팩토리얼
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n-1)

print(factorial_recursive(5))

# 1차원 리스트 초기화
a = [1] * 9
b = [True] * 9
print(a)
print(b)

# 2차원 리스트 초기화
# 리스트 컴프리핸션
# (x, y, z) for x in Iterator for y in Iterator for z in Iterator if _ if _
graph = [[] for _ in range(3)]

# 슬라이스
# arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라
stack = [x for x in range(10)]
print(stack[::-1]) # -1의 간격으로 (= 거꾸로)

# if _ in Iterator
a, b, c = '12', '34', '56'
if '3' in str(a) + str(b) + str(c):
    pass