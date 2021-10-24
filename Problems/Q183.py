# Q183.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-mini-max-sum/problem

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    print(sum(arr[:-1]), sum(arr[1:]))