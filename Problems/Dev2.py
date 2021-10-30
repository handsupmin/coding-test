# Dev2.py

from itertools import combinations

def solution(leave, day, holidays):
    can_rest = set()
    work_date = []
    result = []
    days = dict()
    days['MON'] = (6, 7)
    days['TUE'] = (5, 6)
    days['WED'] = (4, 5)
    days['THU'] = (3, 4)
    days['FRI'] = (2, 3)
    days['SAT'] = (1, 2)
    days['SUN'] = (1, 7)
    a, b = days[day]
    for _ in range(1, 6):
        if a < 31:
            can_rest.add(a)
            a += 7
        if b < 31:
            can_rest.add(b)
            b += 7
    
    for h in holidays:
        can_rest.add(h)
    
    for i in range(1, 31):
        if i not in can_rest:
            work_date.append(i)
    
    if len(work_date) < leave:
        return 30

    for value in list(combinations(work_date, leave)):
        temp_holiday = list(can_rest)[:]
        count = 0
        maximum = 0
        for d in value:
            temp_holiday.append(d)
        temp_holiday.sort()
        for i in range(1, 31):
            if i in temp_holiday:
                count += 1
            else:
                maximum = max(count, maximum)
                count = 0
            if i == 30:
                maximum = max(count, maximum)
        result.append(maximum)
    return max(result)

print(solution(4,	"FRI",	[6, 21, 23, 27, 28]))