# Q031.py
# 럭키 스트레이트
"""
짝수 자릿수 정수인 N이 있다. 왼쪽 각 자릿수의 합과 오른쪽 각 자릿수의 합이 같을 때
럭키 스트레이트 기술을 쓸 수 있다.
"""
n = input()
length = int(len(n)/2)

left = n[:length]
right = n[length:]

left_sum = 0
right_sum = 0

for value in left:
    left_sum += int(value)
for value in right:
    right_sum += int(value)

if left_sum == right_sum:
    print("LUCKY")
else:
    print("READY")

"""
입력 예시 1
123402
출력 예시 1
LUCKY

입력 예시 2
7755
출력 예시 2
READY
"""