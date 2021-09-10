# Q085.py
# https://programmers.co.kr/learn/courses/30/lessons/72411

from itertools import combinations
from collections import defaultdict

def solution(orders, course):
    result = defaultdict(int)
    for i in range(len(orders)):
        order = list(map(str,orders[i]))
        order.sort()
        for n in range(2,len(order)+1):
            if n in course:
                combi = list(map(str, combinations(order, n)))
                for j in range(len(orders)):
                    now_order = list(map(str,orders[j]))
                    now_order.sort()
                    if i == j:
                        continue
                    now = set(now_order)
                    for values in combi:
                        count = 0
                        for value in values:
                            if value in now:
                                count += 1
                        if count == n:
                            result[values] += 1
    
    result_array = [[] for _ in range(20)]
    for key in list(result.keys()):
        result_array[len(key)//5].append((key, result[key]))

    answer_list = []

    for i in range(len(result_array)):
        max_count = 0
        if len(result_array[i]) == 0:
            continue
        result_array[i].sort(reverse= True, key = lambda x : x[1])
        for value, num in result_array[i]:
            if max_count == 0:
                max_count = num
                answer_list.append(value)
            elif num == max_count:
                answer_list.append(value)

    answer = []

    for value in answer_list:
        t = value.replace('"','')        
        t = t.replace("'",'')
        t = t.replace(',','')
        t = t.replace(' ','')
        t = t.replace('(','')
        t = t.replace(')','')
        answer.append(t)

    answer.sort()

    return answer