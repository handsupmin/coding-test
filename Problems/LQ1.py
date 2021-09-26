# Q1.py

def solution(student, k):
    n = len(student)
    index = []
    group = []
    count = 0
    
    for i in range(n):
        if student[i] == 1:
            index.append(i)
    
    index_set = set(index)
    n_index = len(index)
    
    if n_index < k:
        return 0
            
    for i in range(n_index - k + 1):
        group_list = []
        for j in range(k):
            group_list.append(index[i+j])
        group.append(group_list)
        
    for g in group:
        first = g[0]
        last = g[-1]
        count_left = 1
        count_right = 1
        for i in range(first, -1, -1):
            if i == first:
                continue
            if i not in index_set:
                count_left += 1
            else:
                break
        for j in range(last, n):
            if j == last:
                continue
            if j not in index_set:
                count_right += 1
            else:
                break
                
        count += count_left * count_right
        
    return count