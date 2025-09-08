def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5)+1):
        if num % i == 0:
            return False
    return True

n = 20
primes = []
for num in range(2, n+ 1):
    if is_prime(num):
        primes.append(num)

print(f'All prime number from 1 to {n} are : {primes}')

print(f'Alternate prime numbers from 1 to {n}:')

for i in range(0, len(primes), 2):
    print(primes[i])