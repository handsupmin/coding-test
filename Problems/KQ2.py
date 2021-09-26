# KQ2.py

def solution(n, k):
    rev_base = ''
    answer = 0

    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)

    result = rev_base[::-1]

    numbers = list(result.split('0'))

    for num in numbers:
        if len(num) == 0:
            continue
        num = int(num)
        count = 0
        for i in range(2, num+1):
            if i >= 1000000:
                return 1
            if num % i == 0:
                count += 1
                if count >= 2:
                    break
        if count == 1:
            answer += 1


print(solution(1000000, 3))