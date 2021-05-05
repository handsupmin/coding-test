# 그리디
n = 38700 # 주어진 금액에 대하여 최소한의 동전을 이용하여 바꾸어주기
count = 0

# 큰 단위의 화폐부터 차례대로 확인
coin_types = [500, 100, 50, 10]

for coin in coin_types:
    count += n // coin
    n %= coin
    
print(count)