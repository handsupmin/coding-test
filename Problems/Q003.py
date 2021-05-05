# Q003.py
"""
숫자 카드 게임
가장 작은 수를 찾아라!
"""

n, m = map(int, input().split())
maximum = []

for _ in range(n):
    a = list(map(int, input().split()))
    maximum.append(min(a))

print(max(maximum))

    
