# Q041.py
# 자연수를 연속된 자연수들의 합으로 표현할 수 있는 방법의 수
def solution(n):
    count = 0
    for i in range(1, (n//2 + 1)):
        sum_of_num = 0
        for j in range(i, n+1):
            sum_of_num += j
            if sum_of_num == n:
                count += 1
            elif sum_of_num > n:
                break
    return count+1