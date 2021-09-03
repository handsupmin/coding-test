# Q069.py
# https://programmers.co.kr/learn/courses/30/lessons/43165?language=python3

def dfs(numbers, arr):
    if len(numbers) != 0:
        plus = numbers.pop()
        minus = -plus
        if len(arr) == 0:
            arr = dfs(numbers, [plus, minus])
        else:
            t1 = [x + plus for x in arr[:]]
            t2 = [x + minus for x in arr[:]]
            arr = dfs(numbers, t1+t2)
    return arr
        

def solution(numbers, target):        
    return dfs(numbers, []).count(target)