# Q084.py
# https://programmers.co.kr/learn/courses/30/lessons/72410

def solution(new_id):
    can_use = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '-', '_', '.'}
    new_id = new_id.lower()
    
    i = 0
    result = ''
    while i != len(new_id):
        if new_id[i] in can_use:
            result += new_id[i]
        i += 1
        
    while result.find('..') != -1:
        result = result.replace('..','.')
    
    if len(result) >= 1:
        if result[0] == '.':
            if len(result) > 1:
                result = result[1:]
            else:
                result = ''
    if len(result) >= 1:  
        if result[-1] == '.':
            if len(result) > 1:
                result = result[:-1]
            else:
                result = '' 
    
    if len(result) == 0:
        result = 'a'
    
    if len(result) >= 16:
        result = result[:15]
        if result[-1] == '.':
            result = result[:-1]
    
    if len(result) <= 2:
        while len(result) != 3:
            result += result[-1]
            
    return result