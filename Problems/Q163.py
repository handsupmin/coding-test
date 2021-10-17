# Q163.py
# https://www.acmicpc.net/problem/18111

from collections import defaultdict

n, m, inven = map(int, input().split())

ground = []
candidate = defaultdict(int)

for _ in range(n):
    temp = list(map(int, input().split()))
    ground.append(temp)
    for t in temp:
        candidate[t] += 1

result = []
keys = list(candidate.keys())
keys.sort(reverse=True)
for target in range(256, -1, -1):
    is_break = False
    spend = 0
    left = inven
    for k in keys:
        if target == k:
            continue
        if target < k:
            left += (k - target) * candidate[k]
            spend += 2 * (k - target) * candidate[k]
        elif target > k:
            left -= (target - k) * candidate[k]
            if left < 0:
                is_break = True
                break
            spend += (target - k) * candidate[k]
    if is_break:
        continue
    else:
        result.append((spend, target))


result.sort(key = lambda x : (x[0], -x[1]))

print(result[0][0], result[0][1])