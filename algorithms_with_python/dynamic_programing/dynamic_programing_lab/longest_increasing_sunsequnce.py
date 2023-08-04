input_array = [int(i) for i in input().split()]
subsequence = [1] * len(input_array)
path = [-1] * len(input_array)

cur_best_length = 0
cur_best_index = 0

for index_i in range(1, len(input_array)):
    for index_j in range(index_i, -1, -1):

        if input_array[index_i] <= input_array[index_j]:
            continue

        longest_subsequence = subsequence[index_j] + 1
        if longest_subsequence >= subsequence[index_i]:
            subsequence[index_i] = longest_subsequence
            path[index_i] = index_j

        if longest_subsequence > cur_best_length:
            cur_best_length = longest_subsequence
            cur_best_index = index_i

result = []
parent = cur_best_index
while parent != -1:
    result.insert(0, input_array[parent])
    parent = path[parent]

print(*result)