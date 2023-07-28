# quick sort is a a efficient sorting algorithm, it uses recursion and a pivot
# it has a space complexity of O(n*log(n)) and a O(n2), witch is if the pivot 
# divides the sub arrays in to two very unbalanced portions, its a stable 
# sorting algorithm 

def quick_sort(start, end, array):
    if start >= end: # recursive base case
        return
    
    pivot = start
    left = start + 1
    right = end

    while left <= right: 
        if array[left] > array[pivot] > array[right]:
            array[left], array[right] = array[right], array[left]
        if array[left] <= array[pivot]:
            left += 1
        if array[right] >= array[pivot]:
            right -= 1

    array[right], array[pivot] = array[pivot], array[right]

    quick_sort(start, right - 1, array)
    quick_sort(right + 1 , end, array)

    return array


array = [10, 9, 5, 4, 6, 8, 7, 0, 1, 3, 2, 2, 1, 0,]
print(quick_sort(0, len(array) - 1, array))