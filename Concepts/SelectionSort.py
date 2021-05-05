# selectionSort.py
# 선택 정렬
# 시간 복잡도 O(N^2)
array = [7, 8, 5, 9, 0, 3, 1, 6, 2, 4, 8, 8]


for i in range(len(array)):
    minimum = array[i]
    for j in range(i,len(array)):
        if array[j] <= array[i]:
            array[j], array[i] = array[i], array[j]

print(array)