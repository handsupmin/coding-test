# Q113.py
# https://www.acmicpc.net/problem/10809

alpabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
result = [0] * 26

text = input()
for i in range(len(alpabet)):
    result[i] = str(text.find(alpabet[i]))

print(' '.join(result))