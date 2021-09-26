# Q3.py

from collections import deque

def solution(jobs):
    jobs = deque(jobs)
    request_time, required_time, sorted_number, importance = jobs.popleft()
    time = request_time + required_time
    tasks = [0] * 101
    task_times = [0] * 101
    sequence = [sorted_number]
    
    while jobs:
        request_time, required_time, sorted_number, importance = jobs.popleft()
        now_tasks = tasks[sequence[-1]]
        now_times = task_times[sequence[-1]]
        if request_time <= time:
            tasks[sorted_number] += importance
            task_times[sorted_number] += required_time
        else:
            if max(tasks) == 0:
                time = request_time
                tasks[sorted_number] += importance
                task_times[sorted_number] += required_time               
                now_tasks = tasks[sequence[-1]]
                now_times = task_times[sequence[-1]]
            if tasks[sequence[-1]] != 0:
                time += task_times[sequence[-1]]
                tasks[sequence[-1]] -= now_tasks
                task_times[sequence[-1]] -= now_times
            else:
                print(tasks[4])
                now = tasks.index(max(tasks))
                sequence.append(now)
                time += task_times[sequence[-1]]
                tasks[sequence[-1]] -= now_tasks
                task_times[sequence[-1]] -= now_times

    while max(tasks) != 0:
        if tasks[sequence[-1]] != 0:
            time += task_times[sequence[-1]]
            tasks[sequence[-1]] = 0
            task_times[sequence[-1]] = 0
        else:
            now = tasks.index(max(tasks))
            sequence.append(now)
            time += task_times[sequence[-1]]
            tasks[sequence[-1]] = 0
            task_times[sequence[-1]] = 0
    
    return sequence