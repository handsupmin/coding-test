# Dev1.py

def solution(registered_list, new_id):
    num_list = list(map(str, range(0, 10)))
    registered_set = set(registered_list)
    
    s_length = 0

    for i in range(len(new_id)):
        if new_id[i] not in num_list:
            s_length += 1
    print(s_length)
    while True:        
        if new_id not in registered_set:
            return new_id

        S = new_id[:s_length]
        N = new_id[s_length:]
        print(S, N)
        if N == '':
            n = 0
        else:
            n = int(N)
        n += 1
        N1 = str(n)
        new_id = S + N1
        print(new_id)