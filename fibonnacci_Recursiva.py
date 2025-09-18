
import sys
sys.setrecursionlimit(2000) 

memo = {0: 0, 1: 1}

def fibonacci(n):
    if n in memo:
        return memo[n]
    memo[n] = fibonacci(n-1) + fibonacci(n-2)
    return memo[n]


fib_series = [fibonacci(i) for i in range(10000)]


print("Primeros 10:", fib_series[:10])
print("Último número (posición 1000):", fib_series[-1])
