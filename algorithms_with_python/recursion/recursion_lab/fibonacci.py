# finding the n-th fibonacci number using recursion and memoization,
# makes this algorithm preform better then the not memoized one,
# linear solution with a for loop is better

def recursive_fibonacci(n: int, cache = {}) -> int:
    if n in cache:
        return cache[n]
    if n < 2:
        return 1    
    cache[n] = (recursive_fibonacci(n - 1, cache) 
                + recursive_fibonacci(n - 2, cache))
    return cache[n]


fib_number = int(input())
print(recursive_fibonacci(fib_number)) 