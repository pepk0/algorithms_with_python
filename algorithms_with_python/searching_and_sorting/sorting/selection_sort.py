# Selection sort is similar to bubble sort, they have the same time complexity
# which is O(n2) and same space complexity O(1), its a unstable in place 
# algorithm, but we can modify it to be stable by using only < (instead of <=)
# when comparing the values at the indexes.
# we use it when we have a small input array and if space complexity is a issue
# it is also easy to implement.
# we avoid it when dealing with a lot of items, because of its poor time 
# performance

def selection_sort(array: list) -> list:
    
    for i in range(len(array)):
        curr_lowest_index = i
        for j in range(i + 1, len(array)):
            if array[j] < array[curr_lowest_index]:
                curr_lowest_index = j
    
        array[curr_lowest_index], array[i] = array[i], array[curr_lowest_index]

    return array

test_array = [5, 10, 2, 3, 1, 1, 6]
print(selection_sort(test_array))