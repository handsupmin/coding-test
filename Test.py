# Test.py
"""
연습용으로 사용하는 파일입니다.


# 파이썬에서 많은 양의 입력을 받을 때 사용하는 sys.stdin.readline() 함수
# input()은 동작 속도가 느리다.
import sys
# readline시 엔터가 줄바꿈 기호(\n)로 입력되는데, 이를 지우기 위하여 rstrip() 사용

for i in range(10):
    data = sys.stdin.readline().rstrip()

print(data)

"""
# f-string

answer = 7
print(f"정답은 {answer}입니다.")