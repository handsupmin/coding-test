# Q071.py
# https://programmers.co.kr/learn/courses/30/lessons/43163?language=python3

def solution(begin, target, words):
    n = len(target)
    bg = [begin]
    count = 0
    is_done = True
    
    while is_done:
        if target not in words:
            return 0 
        is_done = False
        count += 1
        t_bg = []
        
        for j in range(len(bg)):
            t = bg.pop()
            for word in words:
                ct = 0
                for i in range(n):
                    if word[i] == t[i]:
                        ct += 1
                if ct == n-1:
                    is_done = True
                    t_bg.append(word)
        if target in t_bg:
            return count
        bg = t_bg