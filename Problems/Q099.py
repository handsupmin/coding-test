# Q099.py
# https://www.acmicpc.net/problem/1697

from collections import deque

def bfs(now, visited, target):
    queue = deque([now])
    visited[now] = 0
    while queue:
        value = queue.popleft()
        if value == target:
            return 0
        move_go = value + 1
        move_back = value - 1
        move_jump = value * 2

        if _is_in_range(move_go) and visited[move_go] == -1:
            visited[move_go] = visited[value] + 1
            if move_go == target:
                return visited[move_go]
            queue.append(move_go)
        
        if _is_in_range(move_back) and visited[move_back] == -1:
            visited[move_back] = visited[value] + 1
            if move_back == target:
                return visited[move_back]
            queue.append(move_back)

        if _is_in_range(move_jump) and visited[move_jump] == -1:
            visited[move_jump] = visited[value] + 1
            if move_jump == target:
                return visited[move_jump]
            queue.append(move_jump)


def _is_in_range(num):
    if 0 <= num <= 100000:
        return True
    return False
visited = [-1] * 100001

start, target = map(int, input().split())

print(bfs(start, visited, target))