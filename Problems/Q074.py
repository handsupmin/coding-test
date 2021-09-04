# Q074.py
# https://programmers.co.kr/learn/courses/30/lessons/42839?language=python3

from itertools import permutations

def solution(numbers):
    numbers = list(map(str, numbers))
    n = len(numbers)
    prime_number = set()
    
    for i in range(n):
        candidates = list(permutations(numbers, i+1))
        for candidate in candidates:
            count = 0
            num = int("".join(candidate))
            for i in range(1, num+1):
                if num % i == 0:
                    count += 1
                    if count > 2:
                        break
            if count == 2:
                prime_number.add(num)
    
    return len(prime_number)