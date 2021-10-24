# Dev3.py

from collections import deque

def solution(macaron):
    lines = [[0] * 6 for _ in range(6)]
    heights = [0] * 6
    
    delta = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    for line, color in macaron:
        line -= 1
        visited = set()
        queue = deque()
        is_done = True
        
        x, y = 5 - heights[line], line
        lines[x][y] = color
        heights[y] += 1
        
        queue.append((x, y))
        count = 1
        visited.add((x, y))
        while queue:
            now = queue.pop()
            x, y = now
            for dx, dy in delta:
                nx = x + dx
                ny = y + dy
                if (nx, ny) not in visited and 0 <= ny <= 5 and 0 <= nx <= 5 and lines[nx][ny] == color:
                    count += 1
                    queue.append((nx, ny))
                    visited.add((nx, ny))
                    
        if count >= 3:
            for x, y in visited:
                lines[x][y] = 0
                heights[y] -= 1
            for i in range(5, 0, -1):
                for j in range(6):
                    if lines[i][j] == 0 and lines[i-1][j] != 0:
                        lines[i][j], lines[i-1][j] = lines[i-1][j], lines[i][j]
        else:        
            while is_done:
                for i in range(5, -1, -1):
                    for j in range(6):
                        x, y = i, j
                        if lines[x][y] != 0:
                            visited = set()
                            queue = deque()
                            queue.append((x, y))
                            count = 1
                            visited.add((x, y))
                            while queue:
                                now = queue.pop()
                                x, y = now
                                for dx, dy in delta:
                                    nx = x + dx
                                    ny = y + dy
                                    if (nx, ny) not in visited and 0 <= ny <= 5 and 0 <= nx <= 5 and lines[nx][ny] == color:
                                        count += 1
                                        queue.append((nx, ny))
                                        visited.add((nx, ny))
                            if count >= 3:
                                for x, y in visited:
                                    lines[x][y] = 0
                                    heights[y] -= 1
                                for i in range(5, 0, -1):
                                    for j in range(6):
                                        if lines[i][j] == 0 and lines[i-1][j] != 0:
                                            lines[i][j], lines[i-1][j] = lines[i-1][j], lines[i][j]
                            else:
                                is_done = False
        print(lines)

solution([[1,1],[2,1],[1,2],[3,3],[6,4],[3,1],[3,3],[3,3],[3,4],[2,1]])