# 큰 수의 법칙
"""
N개의 자연수를 배열로 입력받고 주어진 수들을 M번 더하여 가장 큰 수를 만든다.
단, 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없다.
"""

# N, M, K를 공백으로 구분하여 입력받기
n, m, k = map(int, input().split())
# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input().split()))

data.sort() # 입력받은 수들 정렬하기
first = data[n-1] # 가장 큰 수
second = data[n-2] # 두 번째로 큰 수

result = 0

while True:
    for i in range(k): # 가장 큰 수를 K번 더하기
        if(m == 0): # m이 0이면 반복문 탈출
            break;
        result += first
        m -= 1 # 더할 때마다 1씩 빼기
    if(m == 0): # m이 0이라면 반복문 탈출
        break;
    result += second # 두 번때로 큰 수를 한 번 더하기
    m -= 1

print(result) # 최종 결과 출력
