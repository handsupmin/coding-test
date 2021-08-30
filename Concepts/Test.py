# Test.py
# 실험용 파일입니다.

from collections import deque

def solution(board):
    SIZE = len(board)
    OPEN, WALL = range(2)
    ROW_WISE, COLUMN_WISE = range(2)    
    START = (0, 0, ROW_WISE)
    END_POINT = (SIZE-1, SIZE-1)
    DELTAS = ((0,1), (1,0), (0,-1), (-1,0))
    move_count = 0
    
    queue = deque([START])
    visited = set()
    visited.add(START)
    
    def _is_in_range(r, c):
        return 0 <= r < SIZE and 0 <= c < SIZE
    
    def _is_it_open(r, c):
        return board[r][c] == OPEN
    
    def _is_it_ok(r, c):
        return _is_in_range(r, c) and _is_it_open(r, c)
    
    def _yield_row_wise(r, c):
        for dr, dc in DELTAS:
            next_r, next_c = r + dr, c + dc
            if _is_it_ok(next_r, next_c) and _is_it_ok(next_r, next_c+1):
                yield (next_r, next_c, ROW_WISE)
        
        if _is_it_ok(r+1, c) and _is_it_ok(r+1, c+1):
            yield (r, c, COLUMN_WISE)
            yield (r, c+1, COLUMN_WISE)
        if _is_it_ok(r-1, c) and _is_it_ok(r-1, c+1):
            yield (r-1, c, COLUMN_WISE)
            yield (r-1, c+1, COLUMN_WISE)
            
    def _yield_column_wise(r, c):
        for dr, dc in DELTAS:
            next_r, next_c = r + dr, c + dc
            if _is_it_ok(next_r, next_c) and _is_it_ok(next_r+1, next_c):
                yield (next_r, next_c, COLUMN_WISE)
        
        if _is_it_ok(r, c+1) and _is_it_ok(r+1, c+1):
            yield (r, c, ROW_WISE)
            yield (r+1, c, ROW_WISE)
        if _is_it_ok(r, c-1) and _is_it_ok(r+1, c-1):
            yield (r, c-1, ROW_WISE)
            yield (r+1, c-1, ROW_WISE)
            
    while queue:
        move_count += 1
        
        for _ in range(len(queue)):
            r, c, state = queue.popleft()
            
            if state == ROW_WISE:
                yield_function = _yield_row_wise
            else:
                yield_function = _yield_column_wise
                
            for value in yield_function(r, c):
                if value not in visited:
                    queue.append(value)
                    visited.add(value)
                    
                    r, c, state = value
                    if (r+1, c) == END_POINT or (r, c+1) == END_POINT:
                        return move_count