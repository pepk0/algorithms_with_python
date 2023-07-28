# bubble sort is a inplace(meaning no extra space is needed), 
# stable(meaning order is equal items is preserved)  sorting algorithm
# it has a bad time complexity and good space complexity
# we use it only with small and or sorted arrays.

def bubble_sort(array: list) -> list:
    for iterations in range(len(array) -1, 0, -1):
        for index in range(iterations):
            if array[index] > array[index + 1]:
                array[index + 1], array[index] = array[index], array[index + 1]

    return array

list_one = [6,1,5,1,2,-1]
print(bubble_sort(list_one))