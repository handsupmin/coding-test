# Q065.py
# https://programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    n = len(citations)
    citations.sort(reverse = True)
    count = 0
    
    for value in citations:
        count += 1
        if value == count:
            return count
        elif value < count:
            return count - 1
        
    return n