# Q057.py
# https://programmers.co.kr/learn/courses/30/lessons/42584

def solution(prices):
    answer = []
    for i in range(len(prices)-1):
        count = 0
        now = prices[i]
        for j in range(i+1, len(prices)):
            count += 1
            if now <= prices[j]:
                pass
            else:
                break
        answer.append(count)
    answer.append(0)
    
    return answer