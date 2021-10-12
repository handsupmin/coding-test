# Q139.py
# https://www.acmicpc.net/problem/2609

from collections import defaultdict

num1, num2 = map(int, input().split())
d_num1 = defaultdict(int)
d_num2 = defaultdict(int)

while num1 != 1:
    for i in range(2, num1 + 1):
        if num1 % i == 0:
            d_num1[i] += 1
            num1 //= i
            break

while num2 != 1:
    for i in range(2, num2 + 1):
        if num2 % i == 0:
            d_num2[i] += 1
            num2 //= i
            break

gcf = 1
lcm = 1

for num in d_num1:
    if num in d_num2:
        gcf *= (num ** min(d_num1[num], d_num2[num]))

for num in d_num1:
    lcm *= (num ** d_num1[num])
for num in d_num2:
    lcm *= (num ** d_num2[num])
    if num in d_num1:
        lcm //= (num ** min(d_num1[num], d_num2[num]))

print(gcf)
print(lcm)