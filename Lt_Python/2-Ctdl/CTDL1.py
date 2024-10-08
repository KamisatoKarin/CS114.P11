def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def count_prime_sum_pairs(n):
    primes = []
    for i in range(2, n):
        if is_prime(i):
            primes.append(i)
    
    count = 0
    seen = set()
    for prime in primes:
        if n - prime in primes and (n - prime, prime) not in seen:
            count += 1
            seen.add((prime, n - prime))
            seen.add((n - prime, prime))
    
    return count


n = int(input())
print(count_prime_sum_pairs(n))


