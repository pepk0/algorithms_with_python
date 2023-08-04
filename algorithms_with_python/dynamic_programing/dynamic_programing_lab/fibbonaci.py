def fibonacci(num: int, cache = {}) -> int:
    if num in cache:
        return cache[num]
    
    if num <= 1:
        return num
    
    result = fibonacci(num - 1) + fibonacci(num - 2)
    cache[num] = result
    return cache[num]

num = int(input())
print(fibonacci(num))