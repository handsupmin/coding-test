# Q211.py
# https://www.acmicpc.net/problem/5525

n = int(input())
m = int(input())
s = input()
now = 0
result = 0

while now < m:
    count = 0
    if s[now] == 'I':
        if now + 1 < m and s[now + 1] == 'O':
            if now + 2 < m and s[now + 2] == 'I':
                count += 1
                now += 2
                
            else:
                now += 1
                continue

        else:
            now += 1
            continue

    else:
        now += 1
        continue
    
    if not count:
        now += 1
        continue

    else:
        while now < m:
            if now + 1 < m and s[now + 1] == 'O':
                if now + 2 < m and s[now + 2] == 'I':
                    count += 1
                    now += 2

                else:
                    now += 1
                    break

            else:
                now += 1
                break
    
    if count >= n:
        result += count - (n - 1)

print(result)