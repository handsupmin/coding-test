# Q2.py

from collections import defaultdict

def solution(research, n, k):
    n_list = len(research)
    best_keyword = defaultdict(int)
    keywords = defaultdict(int)
    
    date = 0
    for value in research:
        date += 1
        for i in range(len(value)):
            keywords[(date, value[i])] += 1
            
    keys = list(keywords.keys())
    
    for key in keys:
        num = keywords[key]
        day, char = key
        count = 0
        total = 0
        if num >= k and (day + n <= n_list + 1):
            total += num
            count += 1
            for i in range(1, n):
                next_key = ((day + i), char)
                if next_key in keys and keywords[next_key] >= k:
                    total += keywords[next_key]
                    count += 1
                    continue
                else:
                    break
                    
        if count == n and total >= 2 * n * k:
            best_keyword[char] += 1
    
    if len(best_keyword) == 0:
        return "None"
    
    maximum = max(list(best_keyword.values()))
    
    lists = sorted(list(best_keyword.keys()))
    
    for value in lists:
        if best_keyword[value] == maximum:
            return value