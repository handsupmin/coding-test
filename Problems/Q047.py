# Q047.py
# https://programmers.co.kr/learn/courses/30/lessons/42577

def solution(phone_book):
    phone_book.sort()
    for now in range(len(phone_book)-1):
        if phone_book[now] == phone_book[now+1][:len(phone_book[now])]:
            return False
        
    return True