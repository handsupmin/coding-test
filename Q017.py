# Q017.py
"""
개미 전사
일직선 상의 식량 창고에서 식량을 약탈하는 개미전사
단, 연속된 칸에서 식량을 약탈하면 메뚜기 전사에게 들키게 된다.
개미 전사가 정찰병에게 들키지 않고 약탈할 수 있는 최댓값을 구하시오.

점화식으로 문제 해결
"""

n = int(input())
food = list(map(int, input().split()))

d = [0] * 100

d[0] = food[0]
d[1] = max(food[0], food[1])
for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + food[i])

print(d[n-1])

"""
4
1 3 1 5
"""