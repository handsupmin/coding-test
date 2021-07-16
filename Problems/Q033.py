# Q033.py
"""
문자열 압축
https://programmers.co.kr/learn/courses/30/lessons/60057?language=python3
"""
def solution(s):
    minimum = len(s)
    for i in range(len(s)//2):
        result = zip_string(s, i+1)
        if result < minimum:
            minimum = result
    
    return minimum

def zip_string(s, prm):
    now = 0
    count = 1
    s_num = prm
    string = s[now:s_num]
    result = ''
    
    while s_num <= len(s):        
        now += prm
        s_num += prm
        if string == s[now:s_num]:
            count += 1
        else:
            if count > 1:
                result += str(count) + string
            else:
                result += string
            string = s[now:s_num]
            count = 1
    if count > 1:
        result += str(count) + string
    else:
        result += string

    return len(result)