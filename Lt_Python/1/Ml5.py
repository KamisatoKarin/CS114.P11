import math
import sys

def count_tablet_sizes(n):
    count = 0
    n_squared = n ** 2

    limit = int(n / math.sqrt(2))

    for a in range(1, limit + 1):
        b_squared = (n-a)*(n+a)
        b = math.isqrt(b_squared)
        if b * b == b_squared :
            count += 1

    return count

input = sys.stdin.read
n = int(input().strip())  
print(count_tablet_sizes(n))