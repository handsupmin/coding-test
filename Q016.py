# Q016.py
# 1로 만들기
"""
정수 X가 주어질 때 정수 X에 사용할 수 있는 연산은 다음과 같이 4가지이다.
1. X가 5로 나누어떨어지면, 5로 나눈다.
2. X가 3으로 나누어떨어지면, 3으로 나눈다.
3. X가 2로 나누어떨어지면, 2로 나눈다.
4. X에서 1을 뺀다.

정수 X가 주어졌을 때, 연산 4개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.
"""

i = int(input())
d = [0] * 5

def compare(n):
    d[0] = calc(n)
    d[1] = calc(n-1) + 1
    d[2] = calc(n-2) + 2
    d[3] = calc(n-3) + 3
    d[4] = calc(n-4) + 4

    print('result:',min(d))

def calc(n):
    count = 0

    while True:
        print('n:',n)
        if n == 1:
            break
        if n % 30 == 0:
            n = n//30
            count += 3
        elif n % 25 == 0:
            n = n//25
            count += 2 
        elif n % 15 == 0:
            n = n//15
            count += 2
        elif n % 10 == 0:
            n = n//10
            count += 2
        elif n % 6 == 0:
            n = n//6
            count += 2
        elif n % 5 == 0:
            n = n//5
            count += 1
        elif n % 3 == 0:
            n = n//3
            count += 1
        elif n % 2 == 0:
            n = n//2
            count += 1
        else:
            n -= 1
            count += 1
    print('count:',count)
    return count
    
compare(i)