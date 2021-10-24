# Q192.py
# https://www.hackerrank.com/challenges/palindrome-index/problem

def palindromeIndex(s):
    # Write your code here
    if is_palindrome(s) or len(s) == 1:
        return -1

    start = 0
    end = len(s) - 1

    while start <= end:
        if s[start] != s[end]:
            temp = s[:start] + s[start + 1:]
            if is_palindrome(temp):
                return start

            temp = s[:end] + s[end + 1:]
            if is_palindrome(temp):
                return end

        start += 1
        end -= 1

def is_palindrome(s):
    start = 0
    end = len(s) - 1

    while start <= end:
        if s[start] != s[end]:
            return False

        start += 1
        end -= 1

    return True