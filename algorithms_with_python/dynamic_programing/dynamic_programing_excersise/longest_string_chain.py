string_chain = input().split()

length_list = [len(x) for x in string_chain]
subsequence = [1] * len(length_list)
path = [-1] * len(length_list)

longest_subsequence = 0
longest_subsequence_index = 0

for i in range(1, len(length_list)):
    for j in range(i, -1, -1):

        if length_list[i] <= length_list[j]:
            continue

        increasing_sequence = subsequence[j] + 1
        if increasing_sequence >= subsequence[i]:
            subsequence[i] = increasing_sequence
            path[i] = j

        if increasing_sequence > longest_subsequence:
            longest_subsequence = increasing_sequence
            longest_subsequence_index = i

result = []
parent = longest_subsequence_index
while parent != -1:
    result.insert(0, string_chain[parent])
    parent = path[parent]

print(*result)