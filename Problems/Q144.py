# Q144.py
# https://www.acmicpc.net/problem/10250

t = int(input())
for _ in range(t):
    h, w, n = map(int, input().split())
    front_num = str(n % h if n % h != 0 else h)
    back_num = str(((n - 1) // h) + 1)
    if len(back_num) == 1:
        back_num = '0' + back_num
    print(int(front_num + back_num))