# Q042.py

def solution(jobs):
    average = 0
    time = 0
    left = 0
    now = 0
    jobs.sort()
    done = [0] * len(jobs)
    while True:
        if jobs[now][0] == time and done[now] == 0:
            left = jobs[now][1]
            done[now] = 1
        time += 1
        if left != 0:
            left -= 1
            if left == 0:
                done[now] = 1
                average += time - jobs[now][0]
        if left == 0:
            if done.count(1) == len(jobs):                
                break
            minimum = 1001
            for i in range(len(jobs)):
                if jobs[i][1] < minimum and jobs[i][0] <= time and done[i] == 0:      
                    minimum = jobs[i][1]
                    now = i
                    left = jobs[now][1]
                
    answer = average // len(jobs)
    return answer