# Mysql001.py
# https://programmers.co.kr/learn/courses/30/lessons/77487

"""
SELECT * FROM PLACES WHERE HOST_ID in (SELECT HOST_ID FROM PLACES GROUP BY HOST_ID HAVING COUNT(HOST_ID)>1);
"""