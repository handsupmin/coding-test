# Q089.py
# https://programmers.co.kr/learn/courses/30/lessons/42888?language=python3

def solution(record):
    ENTER, LEAVE = range(2)
    user = dict()
    log = []
    answer = []
    for value in record:
        v = value.split()
        state = v[0]
        u_id = v[1]
        if state == 'Enter':
            name = v[2]
            user[u_id] = name
            log.append((ENTER, u_id))
        elif state == 'Leave':
            log.append((LEAVE, u_id))
        else:
            name = v[2]
            del user[u_id]
            user[u_id] = name
            
    for s, uid in log:
        now = ''
        if s == ENTER:
            now = user[uid] + "님이 들어왔습니다."
        else:
            now = user[uid] + "님이 나갔습니다."
        answer.append(now)
    return answer