# Q185.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-lonely-integer/problem

def lonelyinteger(a):
    # Write your code here
    result = set()
    for num in a:
        if num in result:
            result.remove(num)
        else:
            result.add(num)
    return result.pop()