# Q121.py
# https://www.acmicpc.net/problem/1436

n = int(input())
count = 0
start = 666

while True:
    if '666' in str(start):
        count += 1
        if count == n:
            print(start)
            break
    start += 1