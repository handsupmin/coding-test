# Q103.py
# https://www.acmicpc.net/problem/6549

import sys
input = sys.stdin.readline

while True:
    ans = 0
    least = 0
    histo = []
    data = list(map(int, input().split()))
    n = data[0]
    if n == 0:
        break
    for i in range(n):
        histo.append((i, data[i+1]))
    histo.append((n, -1))

    stack = []

    for i in range(0, n+1):
        index, height = histo[i]
        least = index
        while len(stack) != 0 and stack[len(stack)-1][1] > height:
            t_index, t_height = stack.pop()
            ans = max(ans, (index - t_index) * t_height)
            least = t_index
        stack.append((least, height))

    print(ans)
