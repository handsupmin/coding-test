# Q122.py
# https://www.acmicpc.net/problem/2098

num_of_city = int(input())
city_map = []
for _ in range(num_of_city):
    city_map.append(list(map(int, input().split())))

INF = float('inf')
dp = [[INF] * (1 << num_of_city) for _ in range(num_of_city)]
VISIT_ALL = (1 << num_of_city) - 1

def tsp(city, visited):
    if visited == VISIT_ALL:
        return city_map[city][0] or INF
    
    if dp[city][visited] != INF:
        return dp[city][visited]
    
    for next_city in range(num_of_city):
        if visited & (1 << next_city) == 0 and city_map[city][next_city] != 0:
            dp[city][visited] = min(dp[city][visited], tsp(next_city, (visited | 1 << next_city)) + city_map[city][next_city])
    return dp[city][visited]

print(tsp(0, (1 << 0)))