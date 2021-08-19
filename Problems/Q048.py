# Q048.py
# https://programmers.co.kr/learn/courses/30/lessons/42578

def solution(clothes):
    types = []
    cloth = []
    for value in clothes:
        if value[1] in types:
            cloth[types.index(value[1])].append(value[0])
        else:
            types.append(value[1])
            cloth.append([value[0]])
    
    for num in range(len(cloth)):
        cloth[num].append('none')

    answer = 1
    for value in cloth:
        answer *= len(value)
    
    return answer - 1