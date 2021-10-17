# Q157.py
# https://programmers.co.kr/learn/courses/30/lessons/17676

import decimal

def solution(lines):
    logs = []
    maximum = 0
    
    for i in range(len(lines)):
        date, time, spend = lines[i].split()
        hour, minute, sec = time.split(':')
        
        end = int(3600000 * int(hour) + 60000 * int(minute)+ 1000 * decimal.Decimal(sec))
        start = int(end - 1000 * decimal.Decimal(spend[:-1]) + 1)
        
        logs.append([start, end])
        
    logs.sort(key = lambda x : x[0])
    
    for i in range(len(logs)):
        start = logs[i][0]
        end = logs[i][1]
        count_start = 0
        count_end = 0
        
        for j in range(len(logs)):
            n_start = logs[j][0]
            n_end = logs[j][1]
            
            if end + 999 < n_start:
                break
            if start - 999 > n_end:
                continue
            if start <= n_start <= (start + 999) or start <= n_end <= (start + 999) or n_start <= start and (start + 999) <= n_end:
                count_start += 1
            if end <= n_start <= (end + 999) or end <= n_end <= (end + 999) or n_start <= end and (end + 999) <= n_end:
                count_end += 1
        maximum = max(maximum, count_start, count_end)

    return maximum