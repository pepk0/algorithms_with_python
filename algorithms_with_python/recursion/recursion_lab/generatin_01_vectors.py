def gen_vector(argument_list: list, index = 0) -> None:
    if index >= len(argument_list):
        print(*argument_list, sep="")
        return
    
    numbers = [0, 1]
    for number in numbers:
        argument_list[index] = number
        gen_vector(argument_list, index + 1)


argument_list = [None] * int(input())

gen_vector(argument_list)
