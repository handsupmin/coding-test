# KQ3.py
# solve

def solution(fees, records):
    parking = []
    result = []
    cars_index = [-1] * 10000
    now_in = set()
    
    for i in range(len(records)):
        time, car_num, state = map(str, records[i].split())
        if state == 'IN':
            parking.append([car_num, time])
            cars_index[int(car_num)] = len(parking)
            now_in.add(car_num)
        else:
            now = cars_index[int(car_num)] - 1
            in_time = parking[now][1]
            cars_index[int(car_num)] = -1
            now_in.remove(car_num)
            
            in_hour, in_minute = in_time.split(':')
            out_hour, out_minute = time.split(':')
            
            total_time = (int(out_hour) - (int(in_hour))) * 60 + (int(out_minute) - int(in_minute))
            result.append([car_num, total_time])
    
    parking.sort(reverse=True, key = lambda x : x[1])
    while len(now_in) != 0:
        for car, time in parking:
            if car in now_in:
                in_hour, in_minute = time.split(':')
                out_hour, out_minute = 23, 59
                
                total_time = (out_hour - (int(in_hour))) * 60 + (out_minute - int(in_minute))
                result.append([car, total_time])
                now_in.remove(car)
    result.sort()
    totla_minutes = []
    i = 0
    while i < len(result):
        now, time = result[i]
        for j in range(i+1, len(result)):
            if result[j][0] == now:
                time += result[j][1]
                i = j
        totla_minutes.append(time)
        i += 1
    
    total_fee = []

    for minutes in totla_minutes:
        last = minutes - fees[0]
        if last <= 0:
            total_fee.append(fees[1])
        else:
            if last % fees[2] != 0:
                last = last // fees[2] + 1
            else:
                last = last // fees[2]
            total_fee.append((fees[1] + last* fees[3]))


    return total_fee

print(solution([180, 5000, 10, 600],	["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]))