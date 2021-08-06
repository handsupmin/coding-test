# Q043.py
# 5G 기지국

def solution(n, stations, w):
    answer = 0

    lefted = []

    lefted.append((1, stations[0]-w-1))
    if len(stations) == 1:
        lefted.append((stations[0]+w+1, n))
    else:

        for i in range(1, len(stations)):
            lefted.append((stations[i-1]+w+1, stations[i]-w-1))
            if i == len(stations) -1:
                if i + w >= n:
                    break
                else:
                    lefted.append((stations[i]+w+1, n))

    for value in lefted:
        length = value[1] - value[0] + 1        
        answer += length // (w*2+1)

        if length % (w*2+1) != 0:
            answer += 1

    return answer