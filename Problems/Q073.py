# Q073.py
# https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    supo_1 = [1, 2, 3, 4, 5] # 5
    supo_2 = [2, 1, 2, 3, 2, 4, 2, 5] # 8
    supo_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] # 10
    
    score1 = 0
    score2 = 0
    score3 = 0
    
    for i, answer in enumerate(answers):
        if answer == supo_1[i%5]:
            score1 += 1
        if answer == supo_2[i%8]:
            score2 += 1
        if answer == supo_3[i%10]:
            score3 += 1
    
    max_score = max(score1, score2, score3)
    result = []
    if max_score == score1:
        result.append(1)
    if max_score == score2:
        result.append(2)
    if max_score == score3:
        result.append(3)
    return result