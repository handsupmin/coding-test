# Test.py
# 실험용 파일입니다.

def can_go(tickets, target):
        dep = []
        des = []
        done = set()
        n = len(tickets)
        for i in range(n):
            DEPARTURE, DESTINATION = tickets[i]
            dep.append(DEPARTURE)
            des.append(DESTINATION)
        
        count = 0
        dep.sort()
        des.sort()
        for value in des:
            if value not in done:
                done.add(value)
                num1 = dep.count(value)
                num2 = des.count(value)
                print(value, num1, num2)
                if value == target:
                    if (num1-1) != num2:
                        count += 1
                else:
                    if num1 != num2:
                        count += 1
        print(count)
        if count == 1:
            return True
        else:
            return False

print(can_go([["AOO", "BOO"], ["BOO", "COO"], ["COO", "DOO"], ["DOO", "EOO"], ["EOO", "DOO"], ["DOO", "COO"], ["COO", "BOO"], ["BOO", "AOO"]], "AOO"))