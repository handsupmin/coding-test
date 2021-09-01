# Q063.py
# 떡볶이 떡 만들기

n, m = map(int, input().split())
rice_cakes = list(map(int, input().split()))

result = 0
start = 0
end = max(rice_cakes)
temp_result = 0

while True:
    if start > end:
        if temp_result < m:
            while True:
                mid -= 1
                compare_result = 0
                for x in rice_cakes:
                    if x > mid:
                        compare_result += x - mid
                if compare_result > m:
                    result = mid
                    break
        elif temp_result > m:
            while True:
                mid += 1
                compare_result = 0
                for x in rice_cakes:
                    if x > mid:
                        compare_result += x - mid
                if compare_result < m:
                    result = mid-1
                    break
        break
    mid = (start + end) // 2
    temp_result = 0
    for x in rice_cakes:
        if x > mid:
            temp_result += x - mid
    if temp_result == m:
        result = mid
        break
    elif temp_result < m:
        end = mid - 1
        continue
    
    elif temp_result > m:
        start = mid + 1
        continue

print(result)

"""
입력 예시
4 0
19 15 10 17

출력 예시
15
"""