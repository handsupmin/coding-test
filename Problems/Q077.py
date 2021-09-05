# Q077.py
# https://programmers.co.kr/learn/courses/30/lessons/42862

def solution(n, lost, reserve):
    lost = set(lost)
    reserve = set(reserve)
    
    def _is_in_range(i):
        return 1 <= i <= n
    
    def _is_lost(i):
        return i in lost
    
    def _is_ok(i):
        return _is_in_range(i) and _is_lost(i)
    
    can_join = set()
    
    for person in range(1, n+1):
        if (person not in lost and person not in reserve) or (person in reserve and person in lost):
            can_join.add(person)
        elif person in reserve and person not in lost:
            can_join.add(person)
            if _is_ok(person-1) and person-1 not in can_join:
                can_join.add(person-1)
            elif _is_ok(person+1) and person+1 not in can_join:
                can_join.add(person+1)
                
    return len(can_join)