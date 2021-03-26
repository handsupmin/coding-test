# insertionSort.py
# 삽입 정렬

array = [7, 8, 5, 9, 0, 3, 1, 6, 2, 4, 8, 8]
result = []

result.append(array[0])
index = 0

# index를 활용
for i in range(1, len(array)):
    for j in range(0, i):
        if array[i] <= result[0]:
            index = 0
        elif array[i] > result[len(result)-1]:
            index = len(result)
        elif result[j] <= array[i] < result[j+1]:
            index = j+1
    result.insert(index, array[i])

print(result)

# array에서 직접 변경
array = [7, 8, 5, 9, 0, 3, 1, 6, 2, 4, 8, 8]
for i in range(1, len(array)):
    for j in range(i, 0, -1): # i에서 0+1 까지 -1의 간격으로(역순으로)
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break

print(array)

