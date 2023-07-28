# insertion sort is a inplace sorting algorithm with a O(n2) time complexity
# and a O(1) space complexity, its slow but easy to implement but inefficient
 

def insertion_sort(array: list) -> list:
    for i in range(len(array)):
        j = i
        while j > 0 and array[j] < array[j - 1]:
            array[j], array[j - 1] = array[j - 1], array[j]
            j -= 1

    return array

print(insertion_sort([10, 5, 1, 1, 2, 3, 4, 6, 8 ,7]))