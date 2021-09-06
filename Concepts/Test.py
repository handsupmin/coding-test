# Test.py
# 실험용 파일입니다.

def solution(play_time, adv_time, logs):
    play_time = change_sec(play_time)
    adv_time = change_sec(adv_time)
    viewer = [[0] for _ in range(play_time+1)]
    
    for l in logs:
        s1, s2 = change_log(l)
        s2 += 1
        for i in range(s1, s2):
            viewer[i] += 1
            
    print(viewer)   
    
    return ""

def change_sec(time):
    h, m, s = map(int, time.split(':'))
    s += (h * 3600) + (m * 60)
    return s

def change_log(log):
    t1, t2 = log.split('-')
    s1, s2 = change_sec(t1), change_sec(t2)
    return (s1, s2)

def change_hour(time):
    h, m, s = time // 3600, time // 60, time % 60
    return str(h)+":"+str(m)+":"+str(s)

print(solution("02:03:55",	"00:14:15",	["01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]))