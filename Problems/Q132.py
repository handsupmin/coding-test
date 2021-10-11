# Q132.py
# https://www.acmicpc.net/problem/1978

num_bound = 1000
sieve = [False, False] + [True] * (num_bound - 1)
primes = set()

for number in range(2, num_bound+1):
    if sieve[number]:
        primes.add(number)
        for multiple in range(2 * number, num_bound + 1, number):
            sieve[multiple] = False

n = int(input())
count = 0
for num in list(map(int, input().split())):
    if num in primes:
        count += 1

print(count)