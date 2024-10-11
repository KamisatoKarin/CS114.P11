#Bai lam tham khao chatgpt de xu ly so lon bang thu vien decimal
#Bai lam tham khao gitcopilot de xu ly output
#Tham khao wiki https://en.wikipedia.org/wiki/Lychrel_number de hieu ro ve so Lychrel
#va de tim ra upper bound cua viec so sanh so Palindrome
import sys
from decimal import Decimal, getcontext

getcontext().prec = 15_001

def is_palindrome(n):
    s= str(n)
    return s == s[::-1]

def process_number(n):
    max_repetitions = 10001
    max_length = 15000
    results = []
    
    for i in range(max_repetitions):
        if is_palindrome(n):
            sys.stdout.write("NO\n")
            for result in results[1:]: 
                sys.stdout.write(f"{result}\n")
            sys.stdout.write(f"{n}\n")
            return
        results.append(n)
        nrev = Decimal(str(n)[::-1])
        n = n + nrev
        if len(str(n)) >= max_length:
            sys.stdout.write("YES\n")
            sys.stdout.write(f"{i + 1} {n}\n")
            return
    sys.stdout.write("YES\n")
    sys.stdout.write(f"{max_repetitions} {n}\n")
    
if __name__ == "__main__":
    number = Decimal(sys.stdin.readline().strip())
    process_number(number)