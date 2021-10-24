# Q190.py
# https://www.hackerrank.com/challenges/one-week-preparation-kit-caesar-cipher-1/problem

def caesarCipher(s, k):
    # Write your code here
    s = list(s)
    lower_alpha_list = list(string.ascii_lowercase)
    upper_alpha_list = list(string.ascii_uppercase)

    for i in range(len(s)):
        if s[i] in lower_alpha_list:
            s[i] = lower_alpha_list[(lower_alpha_list.index(s[i]) + k) % 26]
        elif s[i] in upper_alpha_list:
            s[i] = upper_alpha_list[(upper_alpha_list.index(s[i]) + k) % 26]
        else:
            continue
        
    return ''.join(s)