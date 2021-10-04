# Q109.py
# https://www.acmicpc.net/problem/2908

n1, n2 = map(str, input().split())

r_n1 = int(n1[2] + n1[1] + n1[0])
r_n2 = int(n2[2] + n2[1] + n2[0])

print(max(r_n1, r_n2))