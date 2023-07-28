def get_factorial(number: int) -> int:
    if number == 0:
        return 1
    
    return number * get_factorial(number - 1)

number = int(input())

print(get_factorial(number))