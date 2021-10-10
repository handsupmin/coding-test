# Q125.py
# https://programmers.co.kr/learn/courses/30/lessons/77484

def solution(lottos, win_nums):
    count_zero = 0
    count_win = 0
    
    for num in lottos:
        if num == 0:
            count_zero += 1
        elif num in win_nums:
            count_win += 1
    
    if count_zero == 0:
        score = get_score(count_win)
        return [score, score]
    else:
        worst = get_score(count_win)
        best = get_score(count_win + count_zero)
        return [best, worst]
    
def get_score(count_win):
    if count_win == 0 or count_win == 1:
        return 6
    else:
        return 7 - count_win