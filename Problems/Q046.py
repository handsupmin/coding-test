# Q046.py
# https://programmers.co.kr/learn/courses/30/lessons/42576

def solution(participant, completion):
    answer = []
    
    participant.sort()
    completion.sort()
    completion.append('hi')
    
    for num in range(len(participant)):
        if participant[num] != completion[num]:
            return participant[num]