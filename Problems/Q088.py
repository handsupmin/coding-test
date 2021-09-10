# Q088.py
# https://programmers.co.kr/learn/courses/30/lessons/72414

def solution(play_time, adv_time, logs):
    play_time = change_sec(play_time)
    adv_time = change_sec(adv_time)
    total_time = [0] * (play_time + 1)
    
    for l in logs:
        s1, s2 = change_log(l)
        total_time[s1] += 1
        total_time[s2] -= 1
        
    for i in range(1, play_time):
        total_time[i] = total_time[i] + total_time[i - 1]
    
    for i in range(1, play_time):
        total_time[i] = total_time[i] + total_time[i - 1]
        
    most_view = 0
    max_time = 0                          
    for i in range(adv_time - 1, play_time):
        if i >= adv_time:
            if most_view < total_time[i] - total_time[i - adv_time]:
                most_view = total_time[i] - total_time[i - adv_time]
                max_time = i - adv_time + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time + 1

    return change_hour(max_time)

def change_sec(time):
    h, m, s = map(int, time.split(':'))
    s += (h * 3600) + (m * 60)
    return s

def change_log(log):
    t1, t2 = log.split('-')
    s1, s2 = change_sec(t1), change_sec(t2)
    return (s1, s2)

def change_hour(time):
    h, m, s = time // 3600, (time % 3600) // 60, time % 60
    h = str(h)
    m = str(m)
    s = str(s)
    if len(h) == 1:
        h = '0' + h
    if len(m) == 1:
        m = '0' + m
    if len(s) == 1:
        s = '0' + s
    return h+":"+m+":"+s