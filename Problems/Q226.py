# Q226.py
# https://www.acmicpc.net/problem/17219

import sys
from collections import defaultdict

input = sys.stdin.readline

n, m = map(int, input().split())

sites = defaultdict(str)

for _ in range(n):
    site, password = input().split()
    sites[site] = password
    
for _ in range(m):
    print(sites[input().rstrip()])