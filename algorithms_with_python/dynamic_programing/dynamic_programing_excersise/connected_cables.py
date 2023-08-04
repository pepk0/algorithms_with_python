def selection_sort(list_arg: list) -> list:

    for i in range(len(list_arg)):
        min_index = i
        for j in range(i, len(list_arg)):
            if list_arg[j] < list_arg[min_index]:
                min_index = j

        list_arg[i], list_arg[min_index] = list_arg[min_index], list_arg[i]

    return list_arg


numbers = [int(i) for i in input().split()]
sorted_nums = selection_sort(numbers.copy())
matrix = [[0] * (len(numbers) + 1) for _ in range(len(sorted_nums) + 1)]

for row in range(1, len(numbers) + 1):
    for col in range(1, len(sorted_nums) + 1):

        if sorted_nums[row - 1] == numbers[col - 1]:
            common_subsequence = matrix[row - 1][col - 1] + 1
            matrix[row][col] = common_subsequence
        else:
            matrix[row][col] = max(matrix[row - 1][col], matrix[row][col - 1]) 

print(f"Maximum pairs connected: {matrix[-1][-1]}")