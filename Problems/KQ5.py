# KQ5.py
from itertools import permutations

def dfs(graph, v, visited, info, state, wolf):
    visited[v] = True
    now_state = 0
    if len(graph[v]) == 0 and info[v] == 0:
        return now_state + 1
    if len(graph[v]) == 0 and info[v] == 1:
        return now_state
    for i in graph[v]:
        if not visited[i]:
            now_state += dfs(graph, i, visited, info, state, wolf)
            break
    if info[v] == 0:
        return now_state + 1
    else:
        wolf.append(v)
        return now_state

def solution(info, edges):
    graph = [[] for _ in range(len(info))]
    visited = [False] * len(info)
    wolf = []
    for parent, child in edges:
        graph[parent].append(child)

    for i in range(len(graph)):
        if len(graph[i]) == 0 and info[i] == 1:
            visited[i] = True

    result = dfs(graph, 0, visited, info, 1, wolf)

    if result > len(wolf) + 1:
        return result
    else:
        maximum = 0
        num_exception = 0
        sheep = []
        for i in range(1, len(info)):
            if info[i] == 0:
                sheep.append(i)
        while True:
            num_exception += 1
            permu = list(permutations(sheep, num_exception))
            for nums in permu:
                visited = [False] * len(info)

                for num in nums:                    
                    visited[num] = True

                wolf = []
                for parent, child in edges:
                    graph[parent].append(child)

                for i in range(len(graph)):
                    if len(graph[i]) == 0 and info[i] == 1:
                        visited[i] = True

                maximum = max(dfs(graph, 0, visited, info, 1, wolf), maximum)
            if maximum != 0:
                return maximum


print(solution([0,1,0,1,1,0,1,0,0,1,0],	[[0,1],[0,2],[1,3],[1,4],[2,5],[2,6],[3,7],[4,8],[6,9],[9,10]]))