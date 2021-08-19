# Q038.py
def solution(arr, divisor):
    answer = []
    for value in arr:
        if value % divisor == 0:
            answer.append(value)
    if len(answer) == 0:
        return [-1]

    answer.sort()
    return answer