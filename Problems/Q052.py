# Q052.py
# 괄호 변환
# https://programmers.co.kr/learn/courses/30/lessons/60058?language=python3

def solution(p):
    if p == '':
        return ''
    num_left = 0
    num_right = 0
    u = ''
    v = ''
    for i in range(len(p)):
        if p[i] == '(':
            num_left += 1
            u += '('
        else:
            num_right += 1
            u += ')'
        if num_left == num_right:
            if i == len(p)-1:
                p = v
                break
            else:
                v = p[i+1:]
                p = v
                break

    if check(u):
        return u + solution(v)
        
    else:
        result = '(' + solution(v) + ')'
        u = u[1:-1]
        t = ''
        for i in range(len(u)):
            if u[i] == '(':
                t += ')'
            else:
                t += '('
        result += t
        return result

def check(p):
    total = 0
    for i in range(len(p)):
        if p[i] == '(':
            total += 1
        else:
            total -= 1
        if total < 0:
            return False
    return True

print(solution("()))((()"))