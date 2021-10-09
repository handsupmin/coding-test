# Q123.py
# https://www.acmicpc.net/problem/1003

dp = [None] * 1001

dp[0] = (1, 0)
dp[1] = (0, 1)

num_of_test = int(input())

def fibonacci(n):
    if n == 0:
        return dp[0]
    elif n == 1:
        return dp[1]
    elif dp[n] != None:
        return dp[n]
    else:
        count1 = fibonacci(n-1)
        count2 = fibonacci(n-2)
        dp[n] = (count1[0]+count2[0], count1[1]+count2[1])
        return dp[n]

for _ in range(num_of_test):
    n = int(input())
    fibonacci(n)
    print(dp[n][0], dp[n][1])