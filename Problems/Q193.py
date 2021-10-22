# Q193.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-recursive-digit-sum/problem

def superDigit(n, k):
    # Write your code here
    numbers = str(sum(list(map(int, n))) * k)
    
    while len(numbers) != 1:
        numbers = str(sum(list(map(int, numbers))))

    return int(numbers)