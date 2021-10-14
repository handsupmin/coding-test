# Q155.py
# https://www.acmicpc.net/problem/2805

n, m = map(int, input().split())

trees = list(map(int, input().split()))

left = 1
right = max(trees)
target = m
while left <= right:
    mid = (left + right) // 2
    total = [tree-mid if tree>mid else 0 for tree in trees]
    total = sum(total)
    if total >= target:
        left = mid + 1
    else:
        right = mid - 1

print(right)