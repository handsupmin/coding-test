# Q182.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-plus-minus/problem

def plusMinus(arr):
    # Write your code here
    arr.sort()
    count_plus = 0
    count_zero = 0
    count_minus = 0
    length = len(arr)
    
    for num in arr:
        if num < 0:
            count_minus += 1
        elif num == 0:
            count_zero += 1
        else:
            count_plus += 1
    
    print(format((count_plus / length), ".6f"))
    print(format((count_minus / length), ".6f"))
    print(format((count_zero / length), ".6f"))