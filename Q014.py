# Q014.py
# 부품 찾기
"""
가게에는 부품이 N개가 있고 해당 부품들은 각자 고유의 부품 번호가 있다.
손님이 M개의 부품을 찾을 때, 해당하는 부품이 있는지 검토하는 코드를 작성하라.
1 <= N <= 1000000
1 <= M <= 100000
"""
n = int(input())
n_list = list(input().split())

m = int(input())
m_list = list(input().split())

def select(ls, start, end, target):
    while start < end:
        mid = (start + end) // 2
        if target == ls[mid] or target == ls[start] or target == ls[end]:
            print("yes", end=" ")
            return
        elif ls[start] < target < ls[mid]:
            end = mid-1
        else:
            start = mid+1
    print("no", end=" ")
    return
        


n_list.sort()

for i in m_list:
    select(n_list, 0, n-1, i)


"""
입력 예시
10
8 3 7 9 2 1 59 36 23 17
5
5 7 9 18 36

출력 예시
no yes yes no yes
"""