# KQ1.py

from collections import defaultdict

def solution(id_list, report, k):
    report_lists = defaultdict(set)
    reported = set()
    result = set()
    tmp = []

    for id in id_list:
        report_lists[id]

    idx = 0

    for i in range(len(report)):
        user1, user2 = report[i].split()
        report_lists[user1].add(user2)
        reported.add(user2)

    for r in reported:
        now = r
        count = 0
        for reporter in report_lists:
            report_list = report_lists[reporter]
            if len(report_list) > 0:
                if now in report_list:
                    count += 1
                    if count >= k:                
                        result.add(r)
                        break
    answer = []

    for key in report_lists:
        number = len(report_lists[key] & result)
        answer.append(number)
    return answer

print(solution(["muzi", "frodo", "apeach", "neo"],	["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],	2))