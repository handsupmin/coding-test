# Q064.py
# https://programmers.co.kr/learn/courses/30/lessons/42746#

def solution(numbers):
    answer = ''
    str_numbers = list(map(str, numbers))
    sorting_list = [[] for _ in range(10)]
    max_digit = len(str(max(numbers)))
    
    for num in str_numbers:
        sorting_list[int(num[0])].append([num, len(num)])
    
    sorting_list.reverse()
    
    for value in sorting_list:
        t_result = ''
        if len(value) != 0:
            for i in range(len(value)):
                if value[i][1] == 1:
                    value[i][0] = value[i][0]*4
                    value[i][1] = -value[i][1]
                elif value[i][1] == 2:
                    value[i][0] = value[i][0][0] + value[i][0][1] + value[i][0][0] * 2
                    if value[i][0][0] < value[i][0][1]:
                        value[i][1] = -value[i][1]
                elif value[i][1] == 3:
                    value[i][0] = value[i][0][0] + value[i][0][1] + value[i][0][2] + value[i][0][0]
                    if value[i][0][0] < value[i][0][1]:
                        value[i][1] = -value[i][1]
            value.sort(reverse = True, key = lambda x : (x[0], x[1]))
            for i in range(len(value)):
                if value[i][1] < 0:
                    value[i][1] = -value[i][1]
            for i in range(len(value)):
                if value[i][1] == 1:
                    value[i][0] = value[i][0][0]
                elif value[i][1] == 2:
                    value[i][0] = value[i][0][0] + value[i][0][1]
                elif value[i][1] == 3:
                    value[i][0] = value[i][0][0] + value[i][0][1] + value[i][0][2]
                answer += value[i][0]
    answer = int(answer)
    answer = str(answer)
                
    return answer