# Q049.py
# https://programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    genre = []
    play = []
    rank = []
    
    for num in range(len(genres)):
        if genres[num] not in genre:
            genre.append(genres[num])
            play.append([(plays[num],num)])
            rank.append(plays[num])
        else:
            play[genre.index(genres[num])].append((plays[num],num))
            rank[genre.index(genres[num])] += plays[num]
    
    for num in range(len(play)):
        play[num].sort(reverse = True)
        if len(play[num]) > 1:
            if play[num][0][0] == play[num][1][0] and play[num][0][1] > play[num][1][1]:
                play[num][0], play[num][1] = play[num][1], play[num][0]

    answer = []
    
    while sum(rank) != 0:
        num = rank.index(max(rank))
        count = 0
        for value in play[num]:
            answer.append(value[1])
            count += 1
            if count == 2:
                break
        rank[num] = 0
                
    return answer