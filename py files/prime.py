def isPrime(n):
    if(n == 4):
        return False
    for i in range(2,int(n/2)):
        if(n/i % 1 == 0):
            return False
    return True

primes = []

for i in range(2,int(input())):
    if(isPrime(i)):
        primes.append(i)

print(primes)