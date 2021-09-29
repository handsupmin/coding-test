# Q096.py
# https://www.acmicpc.net/problem/1157

from collections import defaultdict

words = defaultdict(int)

keyword = list(map(str, input()))

for w in keyword:
    words[w.upper()] += 1

maximum = max(list(words.values()))
if list(words.values()).count(maximum) >= 2:
    print("?")
else:
    print(list(words.keys())[list(words.values()).index(maximum)])