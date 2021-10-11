# note.py
# 배운 것을 기록하는 노트입니다.

# 시간 측정
import time
start = time.time()  # 시작 시간 저장 
# 작업 코드 # 
print("time :", time.time() - start)  # 현재시각 - 시작시간 = 실행 시간

# 문자 입력 받기
n, m, k = map(int,input().split())
a = list(map(int,input().split()))

# .split()을 빼면 한자리씩 리스트에 넣는다
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

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

# deque
from collections import deque
dq = deque()
dq.append(5)
dq.append(4)
dq.append(3)
dq.popleft() # 5
dq.pop() # 3

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

# 주의
graph = [[] * (n + 1)] * (n + 1)
# 이런식으로 쓰면 안됨, 모든 줄이 같은 메모리를 참조하게 됨 (graph[1], graph[2], ...)

# 슬라이스
# arr[A:B:C]의 의미는, index A 부터 index B 까지 C의 간격으로 배열을 만들어라
stack = [x for x in range(10)]
print(stack[::-1]) # -1의 간격으로 (= 거꾸로)

# if _ in Iterator
a, b, c = '12', '34', '56'
if '3' in str(a) + str(b) + str(c):
    pass

# range의 3번째 매개 변수
for j in range(i, 0, -1): # i부터 0+1까지 -1씩
    pass

# 정렬 관련 arguments
def setting(data):
    return data[1]

# key에는 기준이 되는 함수가 들어간다.
array = sorted(stack, key = setting, reverse = True)
# lambda 사용 (lambda 인자 : 표현식)
# ex) lambda x, y : x+y+1
array = sorted(array, key = lambda x:x[1], reverse = True) 

# 튜플 받기
array = [(1, 2)]
a, b = array[0][0], array[0][1]
print(a, b)
import heapq
q = []
heapq.heappush(q, (1, 2))
a, b = heapq.heappop(q) # a = 1, b = 2

# 순열
from itertools import permutations

list(permutations([1,2,3,4], 2))

# [(1, 2), (1, 3), (1, 4), (2, 1), (2, 3), (2, 4), (3, 1), (3, 2), (3, 4), (4, 1), (4, 2), (4, 3)]


# 중복 순열
from itertools import product

list(product([1,2,3,4], repeat=2))

# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

# 조합
from itertools import combinations

list(combinations([1,2,3,4], 2))

# [(1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4)]

# 중복 조합
from itertools import combinations_with_replacement

list(combinations_with_replacement([1,2,3,4], 2))

# [(1, 1), (1, 2), (1, 3), (1, 4), (2, 1), (2, 2), (2, 3), (2, 4), (3, 1), (3, 2), (3, 3), (3, 4), (4, 1), (4, 2), (4, 3), (4, 4)]

# open = 0, wall = 1
OPEN, WALL = range(2)

for i in [-1, 1]:
    pass

def get_next_pos():
    return [-1, 1]

for next_pos in get_next_pos():
    pass

# 문자열
# 문자열 바꾸기
'Hello, world!'.replace('world', 'Python')
'Hello, Python!'

# 문자 바꾸기
table = str.maketrans('aeiou', '12345')
'apple'.translate(table)
'1ppl2'
# 문자열 분리하기
'apple pear grape pineapple orange'.split()
['apple', 'pear', 'grape', 'pineapple', 'orange']

# 구분자 문자열과 문자열 리스트 연결하기
' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])
'apple pear grape pineapple orange'

# 소문자를 대문자로 바꾸기
'python'.upper()
'PYTHON'

# 대문자를 소문자로 바꾸기
'PYTHON'.lower()
'python'

# 왼쪽 공백 삭제하기
'   Python   '.lstrip()
'Python   '

# 오른쪽 공백 삭제하기
'   Python   '.rstrip()
'   Python'

# 양쪽 공백 삭제하기
'   Python   '.strip()
'Python'

# 왼쪽, 오른쪽, 양쪽의 특정 문자 삭제하기
', python.'.lstrip(',.') # rstrip, strip
' python.'

# 특수문자
import string
string.punctuation
'!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

#  문자열 위치 찾기
'apple pineapple'.find('pl')
2
'apple pineapple'.find('xy')
-1

# 오른쪽에서부터 문자열 위치 찾기
'apple pineapple'.rfind('pl')
12
'apple pineapple'.rfind('xy')
-1

# 문자열 위치 찾기(없으면 에러)
'apple pineapple'.index('pl')
2

# format 메서드 사용하기
'Hello, {0} {2} {1}'.format('Python', 'Script', 3.6)
'Hello, Python 3.6 Script'
'Hello, {language} {version}'.format(language='Python', version=3.6)
'Hello, Python 3.6'
'Hello, {} {} {}'.format('Python', 'Script', 3.6)
'Hello, Python Script 3.6'

language = 'Python'
version = 3.6
f'Hello, {language} {version}'
'Hello, Python 3.6'

# sort 다중 조건
# 정렬 기준으로 다중 조건을 넘겨줄 수도 있다
# 첫 번째 인자를 기준으로 오름차순 정렬을 먼저 한다.
# 그 결과를 가지고 두 번째 인자를 기준으로 내림차순 정렬(-를 붙이면 내림차순 정렬)
e = sorted(a, key = lambda x : (x[0], -x[1]))
print(e)    # [(1, 0), (2, 1), (3, 2), (4, 3), (4, 2), (4, 0)]

# copy
import copy
a = [[1,2],[3,4]]
b = copy.deepcopy(a)

# defaultdict
from collections import defaultdict
list_dict = defaultdict(list)
lists = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]
for l in lists:
    list_dict[l[0]].append(l[1])
{'ICN': ['SFO', 'ATL'], 'SFO': ['ATL'], 'ATL': ['ICN', 'SFO']}

# enumerate() 
# index와 쌍을 이루는 튜플 리턴
# enumerate(iter, start = 1), 1부터 시작
for entry in enumerate(['A', 'B', 'C']):
    print(entry)

(0, 'A')
(1, 'B')
(2, 'C')

# bisect은 이진 검색 알고리즘을 지원
# 이진 검색 알고리즘이 깔끔하게 모듈 형태로 구현되어 있음
# 정렬된 리스트 a 에 데이터 x을 삽입한다 가정
# bisect_left(a, x) 
# -> 정렬 된 순서를 유지하며 a에 x를 삽입할 때, 가장 왼쪽 인덱스 반환
# bisect_right(a, x)
# -> 정렬 된 순서를 유지하며 a에 x를 삽입할 때, 가장 오른쪽 인덱스 반환

import bisect

nums = [1,2,3,3,3,5,6,8,9]
nums.sort() #binary search는 정렬 된 배열에서 사용해야함

print(bisect.bisect_left(nums, 10)) # 9
print(bisect.bisect_right(nums, 10)) # 9

print(bisect.bisect_left(nums, 3))   # 2
print(bisect.bisect_right(nums, 3))  # 5

# 삼항 연산자
1 if n & (1 << nth) else 0

# 2진수
bin(3) # 0b11
2 << 1 # 4
a = 0b011010 # 0bxxxxx

# 비트 연산
1 << n # bit shift

"""
&	AND 연산. 둘다 참일때만 만족	(a & b) = 12 → 0000 1100
|	OR 연산. 둘 중 하나만 참이여도 만족	(a | b) = 61 → 0011 1101
^	XOR 연산. 둘 중 하나만 참일 때 만족	(a ^ b) = 49 → 0011 0001
~	보수 연산.	(~a) = -61 → 1100 0011
<<	왼쪽 시프트 연산자. 변수의 값을 왼쪽으로 지정된 비트 수 만큼 이동	a << 2 = 240 → 1111 0000
>>	오른쪽 시프트 연산자. 변수의 값을 오른쪽으로 지정된 비트 수 만큼 이동	a >> 2 = 15 → 0000 1111
"""

# 정수의 2의 지수승 여부 확인하기
def is_exp_binary(n):
    return n & (n - 1) == 0
    #  1000(2)
    # & 111(2)
    # --------
    #  0000(2)

# 2진수에서 1 비트의 개수 구하기
def bit_count(n):
    k = 0
    count = 0

    while n >= (1 << k):
        if n & (1 << k) != 0:
            count += 1
        k += 1

    return count

# Boolean값 Toggle하기
onoff ^= True

# 비트 끄기
def diff(n, d):
    return n & ~(1 << d)

# or의 활용
print(False or 'this') # False(0) or X 일 시, X가 출력된다

# INF를 math 모듈 없이 사용
float('inf')

# Counter 클래스
# 최빈값
# Counter는 사전(dict) 클래스의 하위 클래스
# 리스트나 튜플에서 각 데이터가 등장한 횟수를 사전 형식으로 돌려준다.

from collections import Counter
colors = ['red', 'blue', 'red', 'green', 'blue', 'blue']
cnt = Counter(colors)
# Counter({'blue': 3, 'red': 2, 'green': 1})

# most_common()
# 등장한 횟수를 내림차순으로 정리하여 다음과 같이 보여준다

numbers = [1, 2, 3, 3, 4, 4, 4, 5, 5]
from collections import Counter
cnt = Counter(numbers)
cnt.most_common()

# (숫자, 횟수)
# [(4, 3), (3, 2), (5, 2), (1, 1), (2, 1)]

# 상위 3개의 값
cnt.most_common(3)
# [(4, 3), (3, 2), (5, 2)]

# 반올림
# 파이썬에 내장된 round() 함수를 사용

round(3.1415, 2)   #결과는 3.14
round(31.415, -1)  #결과는 30.0
"""
사사오입 원칙
round()는 사사오입 원칙을 따른다.
반올림할 자리의 수가 5이면
앞자리의 숫자가 짝수면 내림하고 홀수면 올림 한다.
"""
round(4.5)  #결과는 4
round(3.5)  #결과는 4


# 올림
import math
math.ceil(-3.14)  #결과는 -3
math.ceil(3.14)   #결과는 4
# 내림
import math
math.floor(3.14)   #결과는 3
math.floor(-3.14)  #결과는 -4