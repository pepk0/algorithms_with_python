# solution 1, using recursion and head tail method 

# def recursive_reverse(array: list) -> list:
    
#     if len(array) == 1:
#         return array
    
#     head = array[0]
#     tail = array[1:]

#     return recursive_reverse(tail) + [head]

# solution 2, using iteration

# def iterative_reverse(array: list) -> list:
#     iterations = len(array) // 2
#     pointer_i = 0
#     pointer_j = -1

#     for _ in range(iterations):
#         array[pointer_i], array[pointer_j] = array[pointer_j], array[pointer_i]
#         pointer_i += 1
#         pointer_j += -1

#     return array

def recursive_reverse(array: list, index_i = 0, index_j = -1) -> list:
    divided_array = len(array) // 2
    if index_i == divided_array:
        return array
    
    array[index_i], array[index_j] = array[index_j], array[index_i]
    
    return recursive_reverse(array, index_i + 1, index_j + -1)   
    

to_reverse = [int(i) for i in input().split()]
print(*recursive_reverse(to_reverse), sep=" ")
