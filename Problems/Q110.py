# Q110.py
# https://www.acmicpc.net/problem/2920

music = list(map(int, input().split()))

asc = 0
de = 0

for i in range(8):
    if music[i] == i + 1:
        asc += 1
    elif music[i] == 8 - i:
        de += 1

if asc == 8:
    print("ascending")
elif de == 8:
    print("descending")
else:
    print("mixed")
