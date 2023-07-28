def generate_loops(array: list, number: int, index: int = 0) -> None:
    
    if index >= number:
        print(*array, sep=" ")
        return
    
    for num in range(1, number + 1):
        array[index] = num
        generate_loops(array, number, index + 1)


number = int(input())
answer_array = [None] * number
generate_loops(answer_array, number)