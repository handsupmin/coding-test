# Q026.py
"""
곱하기 혹은 더하기
왼쪽에서부터 순서대로 숫자 사이에 곱하기 혹은 더하기를 넣어 가장 큰 결괏값이 나오게 하라.
"""
a = list(map(int,input()))

num1 = a[0]
result = 0

for i in a[1:]:
    num2 = i
    result = num1 * num2
    if (result == 0):
        result = num1 + num2
    num1 = result

print(result)

"""
입력 예시
02984
출력 예시
576

입력 예시
567
출력 예시
210
"""