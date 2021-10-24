# Q191.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-grid-challenge/problem

def gridChallenge(grid):
    # Write your code here
    length = len(grid[0])

    for i in range(n):
        temp = list(grid[i])
        temp.sort()
        grid[i] = ''.join(temp)

    for i in range(length):
        for j in range(n - 1):
            if grid[j][i] > grid[j + 1][i]:
                return 'NO'
                
    return 'YES'