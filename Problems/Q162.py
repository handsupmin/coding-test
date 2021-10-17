# Q162.py
# https://www.acmicpc.net/problem/15829

import string

lower_alpha_list = [0] + list(string.ascii_lowercase)

l = int(input())
value = list(map(str,input()))
result = 0

for i in range(l):
    result += lower_alpha_list.index(value[i]) * (31 ** i)

result %= 1234567891
print(result)