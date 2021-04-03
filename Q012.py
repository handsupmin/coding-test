# Q012.py
# 성적이 낮은 순서로 학생 출력하기

n = int(input())

array = []
for _ in range(n):
    x, y = map(str,input().split())
    array.append((x,int(y)))

# 최초 작성 코드
"""
def setting(data):
    return data[1]

array = sorted(array, key = setting)
"""
# lambda 함수 사용
array = sorted(array, key = lambda x : x[1])

for x in array:
    print(x[0], end = " ")

"""
5
홍길동 95
이순신 77
장영실 65
박새봄 100
허대현 5
"""