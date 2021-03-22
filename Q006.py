# Q006.py

"""
정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는 모든 경우의 수를 구하는 프로그램을 작성하시오.
"""

n = int(input())

hour, minute, second = 0, 0, 0
count = 0

while True:
    # if (str(hour).count('3') >= 1 or str(minute).count('3') >= 1 or str(second).count('3') >= 1): 처음에 짰던 코드
    if '3' in str(hour) + str(minute) + str(second): # 유려하게 바꿔본 코드
        count += 1
    second += 1
    if second == 60:
        minute += 1
        second = 0
    if minute == 60:
        hour += 1
        minute = 0
    if hour == n and minute == 59 and second == 59:
        break

print(count)