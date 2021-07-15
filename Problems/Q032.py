# Q032.py
"""
문자열 재정렬
알파벳과 대문자의 조합을 알파벳이 오름차순으로 정렬되어 출력한 후 숫자를 더한 값을 이어서 출력
"""
import heapq

string = input()
alpha = []
number = []
result = ''

for i in string:
    if i == '0' or i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9':
        number.append(int(i))
    else:
        heapq.heappush(alpha, i)

while alpha:
    result += heapq.heappop(alpha)

result += str(sum(number))

print(result)

"""
입력 예시 1
K1KA5CB7
출력 예시 1
ABCKK13

입력 예시 2
AJKDLSI412K4JSJ9D
출력 예시 2
ADDIJJJKKLSS20
"""