# Q078.py
# https://programmers.co.kr/learn/courses/30/lessons/42860?language=python3

from collections import defaultdict

def solution(name):
    n = len(name)
    alphabet = defaultdict(int)
    alphabet_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    
    for i, char in enumerate(alphabet_list):
        if i <= 13:
            alphabet[char] += i
        else:
            alphabet[char] += 26 - i
        
    visited = [0] * n
    for i in range(n):
        if name[i] == 'A':
            visited[i] = 1
    count = 0
    now = 0
    if visited[0] == 1:
        for i in range(1, n):
            if visited[i] == 0:
                now = i
                count += i
                break
    while True:
        if visited[now] == 0:
            go = 0
            back = 0
            count += alphabet[name[now]]
            visited[now] = 1
            
            if visited.count(1) == n:
                return count
            for i in range(1, n-now):
                if visited[now + i] == 0:
                    go = i
                if visited[now - i] == 0:
                    back = i
                if go != 0 and back != 0:
                    if visited.count(1) == n - 1:
                        next_move = now + go
                        count += go
                        break
                    n_go = 0
                    n_back = 0
                    for j in range(1, n-now):
                        if visited[now + go + j] == 0:
                            n_go = j
                        if visited[now - back - j] == 0:
                            n_back = j
                        if n_go != 0 and n_back != 0:
                            next_move = now + go
                            count += go
                            break
                        elif n_back != 0:
                            next_move = now + go
                            count += go
                            break
                        elif n_back != 0:
                            next_move = now - back
                            count += back
                            break
                    break
                elif go != 0:
                    next_move = now + go
                    count += go
                    break
                elif back != 0:
                    next_move = now - back
                    count += back
                    break
            now = next_move