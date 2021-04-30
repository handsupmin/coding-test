# Test.py
# 실험용 파일입니다.

t = int(input())
array = []
for _ in range(t):
    array.append(list(map(int, input().split())))

for i in array:
    b = i[1] - i[0]
    
    t = 1
    d = 1
    count = 1
    while d <= b:
        d += t
        count += 1
        if d > b:
            break
        d += t
        count += 1
        t += 1
    print(count-1)