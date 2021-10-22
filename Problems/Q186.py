# Q186.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-diagonal-difference/problem

def diagonalDifference(arr):
    # Write your code here
    left = 0
    right = 0
    
    for i in range(n):
        left += arr[i][i]
        right += arr[i][n-i-1]
        
    return abs(left - right)