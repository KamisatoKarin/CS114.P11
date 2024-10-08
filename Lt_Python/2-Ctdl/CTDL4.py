#Bai lam tham khao chatgpt de xu ly so lon bang thu vien decimal
#Bai lam tham khao gitcopilot de xu ly output
#Tham khao wiki https://en.wikipedia.org/wiki/Lychrel_number de hieu ro ve so Lychrel
#va de tim ra upper bound cua viec so sanh so Palindrome
import sys
from decimal import Decimal, getcontext

getcontext().prec = 15_001

def is_palindrome(n):
    n = str(n)  
    return n == n[::-1]

n = Decimal(sys.stdin.readline().strip())
max_repetitions = 10001
max_length = 15000
repi = 0
results = [None] *max_repetitions

while len(str(n)) <= max_length and repi < max_repetitions:
    nrev = Decimal(str(n)[::-1])
    n = n + nrev
    results[repi] = n

    if is_palindrome(n): 
        break
    repi += 1
    
output = []
if is_palindrome(n):
    output.append("NO")
    output.extend(map(str, results[:repi+1]))
else:
    output.append("YES")
    output.append(f"{repi} {n}")  
sys.stdout.write('\n'.join(output) + '\n')