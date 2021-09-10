# Test.py
# 실험용 파일입니다.

def solution(info, query):
    result = []
    infos = []
    
    for value in info:
        lan, job, career, food, score = map(str, value.split())
        infos.append((set([lan, job, career, food]),int(score)))
    infos.sort(reverse = True, key = lambda x: x[1])
    n = len(infos)
    
    for value in query:
        list_value = list(map(str, value.replace("and",'').replace("-",'').split()))
        q = set(list_value[:-1])
        k = len(q)
        score = int(list_value[-1])
        
        count = 0
        if k == 0:
            for i in range(n):
                if score <= infos[i][1]:
                    count += 1
                else:
                    break
        else:
            for i in range(n):
                if score <= infos[i][1]:
                    if len(infos[i][0] & q) == k:
                        count += 1
                else:
                    break
                
        result.append(count)

    return result