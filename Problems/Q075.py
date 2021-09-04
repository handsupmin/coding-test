# Q075.py
# https://programmers.co.kr/learn/courses/30/lessons/42842

def solution(brown, yellow):
    BROWN, YELLOW = range(2)
    for height in range(1, yellow+1):
        if yellow % height == 0:
            width = yellow // height
            if height > width:
                break
            carpet = [[0] * (width + 2) for _ in range(height + 2)]
            count = 0
            for i in range(1, height+1):
                for j in range(1, width + 1):
                    carpet[i][j] = YELLOW
            for i in range(height + 2):
                for j in range(width + 2):
                    if carpet[i][j] == BROWN:
                        count += 1
            if count == brown:
                return [width + 2, height + 2]