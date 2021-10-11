# Eratosthenes.py

num_bound = 1000
sieve = [False, False] + [True] * (num_bound - 1)
primes = []

for number in range(2, num_bound+1):
    if sieve[number]:
        primes.append(number)
        for multiple in range(2 * number, num_bound + 1, number):
            sieve[multiple] = False

print(primes)