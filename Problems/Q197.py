# Q197.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-balanced-brackets/problem

def isBalanced(s):
    # Write your code here
    queue = []
    front = dict()
    
    front['('] = ')'
    front['{'] = '}'
    front['['] = ']'
    
    for bracket in s:
        if bracket in front:
            queue.append(bracket)
        else:
            if len(queue) == 0:
                return 'NO'
            elif front[queue[-1]] != bracket:
                return 'NO'
            else:
                queue.pop()
    if len(queue) != 0:
        return 'NO'
    return 'YES'