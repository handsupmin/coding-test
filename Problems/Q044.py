# Q044.py
# 외벽 점검
# https://programmers.co.kr/learn/courses/30/lessons/60062?language=python3

from itertools import permutations

def solution(n, weak, dist):
    minimum = 1000
    length = len(weak)
    for i in range(length):
        weak.append(weak[i]+n)
    for i in range(len(weak)//2):
        temp = weak[i:i+len(weak)//2]
        for j in range(len(dist)):
            member = list(permutations(dist, j+1))
            for people in member:
                if minimum <= len(people):
                    break
                now = -1
                for person in people:
                    for value in temp:
                        if value <= now:
                            continue
                        else:
                            now = value + person
                            break
                    if now >= max(temp):
                        minimum = min(minimum, len(people))
    
    if minimum > len(dist):
        return -1
    else:
        return minimum