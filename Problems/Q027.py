# Q027.py
"""
문자열 뒤집기
0 또는 1으로 된 문자열 S가 주어졌을 때, 모든 숫자가 같도록 만들려고 한다.
이때 최소한으로 뒤집어야 할 횟수를 구하라.
"""
s = list(map(int,input()))
count0 = 0
count1 = 0
now = -1

for i in s:
    if now == i:
        continue
    else:
        now = i
        if i == 0:
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))

"""
입력 예시
0001100
출력 예시
1

입력 예시
000110011000100101010000111000
출력 예시
7
"""