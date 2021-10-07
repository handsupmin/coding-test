# Q118.py
# https://www.acmicpc.net/problem/1085

x, y, w, h = map(int, input().split())

print(min(abs(x - w), abs(y - h), x, y))