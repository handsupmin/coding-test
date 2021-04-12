# Q013.py
# 두 배열의 원소 교체

"""
원소의 개수가 N개인 자연수 배열 A과 B가 있다.
배열 A와 B의 원소를 K번 바꿀 수 있다. 배열 A의 합이최대가 되도록 원소를 교체해라.
"""

n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort(reverse = True)

for i in range(k):
    if A[i] < B[i]:
        A[i], B[i] = B[i], A[i]

print(sum(A))

"""
5 3
1 2 5 4 3
5 5 6 6 5
"""