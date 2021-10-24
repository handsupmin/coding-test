# Q187.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-countingsort1/problem

def countingSort(arr):
    # Write your code here
    array = [0] * 100
    
    for num in arr:
        array[num] += 1
        
    return array