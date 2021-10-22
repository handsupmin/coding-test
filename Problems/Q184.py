# Q184.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-time-conversion/problem

def timeConversion(s):
    # Write your code here
    hour = s[0:2]
    minute = s[3:5]
    sec = s[6:8]
    ampm = s[8:]
    
    if ampm == 'AM':
        if hour == '12':
            hour = '00'
    else:
        if hour != '12':
            hour = str(int(hour) + 12)
            
    return f'{hour}:{minute}:{sec}'