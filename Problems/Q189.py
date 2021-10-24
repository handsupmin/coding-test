# Q189.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-tower-breakers-1/problem

def towerBreakers(n, m):
    # Write your code here
    if n == 1:
        return 1

    if m == 1:
        return 2

    if n % 2 == 0:
        return 2
        
    else:
        return 1