def sum_array_elements(argument_list: list) -> int:
    if len(argument_list) == 0:
        return 0
    head = argument_list.pop(0)
    return head + sum_array_elements(argument_list)

argument_list = [int(x) for x in input().split()]

print(sum_array_elements(argument_list))