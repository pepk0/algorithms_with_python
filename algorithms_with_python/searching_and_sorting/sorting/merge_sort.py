# merge sort is a efficient sorting algorithm that uses recursion to divide the
# the array in to smaller arrays and them merges them back in order:
# it uses recursion:
# first we divide the original array in to arrays with length of 1
# sort each sub array recursively (calling a merge helper function)
# merge sorts every sub array in the one  single array:
# time complexity O(n*log(n)), space complexity O(n*log(n))-can be made in to
#  O(n)
# we can use this for large input arrays

def merge(left: list, right: list) -> list:
    sorted_array = []
    pointer_i = 0
    pointer_j = 0

    while pointer_i < len(left) and pointer_j < len(right):
        
        if left[pointer_i] < right[pointer_j]:
            sorted_array.append(left[pointer_i])
            pointer_i += 1
        else:
            sorted_array.append(right[pointer_j])
            pointer_j += 1

    while pointer_i < len(left):
        sorted_array.append(left[pointer_i])
        pointer_i += 1
    
    while pointer_j < len(right):
        sorted_array.append(right[pointer_j])
        pointer_j += 1

    return sorted_array


def merge_sort(array: list) -> list:
    
    if len(array) == 1: # recursive base case
        return array
    
    middle = len(array) // 2

    left_array = merge_sort(array[middle:])
    right_array = merge_sort(array[:middle])

    return merge(left_array, right_array)


array = [int(x) for x in input().split()]
print(*merge_sort(array), sep=" ")