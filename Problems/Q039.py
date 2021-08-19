# Q039.py
def solution(n):
    to_string = list(str(n))
    to_string.sort(reverse = True)
    result = ''
    for value in to_string:
        result += value
    answer = int(result)
    return answer