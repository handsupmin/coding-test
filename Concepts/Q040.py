# Q040.py
# 피보나치 수열의 n 번째 수를 1234567로 나눈 나머지
def solution(n):
    dx = [0] * (n + 1)
    dx[0] = 0
    dx[1] = 1

    for i in range(2, n+1):
        dx[i] = dx[i-1] + dx[i-2]

    answer = dx[n] % 1234567
    return answer