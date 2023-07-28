def binary_search(array: list, target: int):
    left_pointer = 0
    right_pointer = len(array) - 1

    while left_pointer <= right_pointer:
        middle_pointer = (left_pointer + right_pointer) // 2

        if array[middle_pointer] > target:
            right_pointer = middle_pointer - 1
        elif array[middle_pointer] < target:
            left_pointer = middle_pointer + 1
        else:
            return middle_pointer
    return -1


array = [1,2,3,4,5,6,7,8,9,10,11]
print(binary_search(array, 9))