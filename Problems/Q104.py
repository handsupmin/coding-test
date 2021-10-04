# Q104.py
# https://www.acmicpc.net/problem/1546

n = int(input())
score = list(map(int, input().split()))

maximum = max(score)

fack_score = [x / maximum * 100 for x in score]

print(sum(fack_score)/len(fack_score))