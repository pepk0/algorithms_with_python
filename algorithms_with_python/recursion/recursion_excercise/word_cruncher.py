def find_combinations(idx, target, words_by_index, words_count, used_words):

    if idx >= len(target):
        print(*used_words, sep=" ")
        return
    
    if idx not in words_by_index:
        return
    
    for word in words_by_index[idx]:
        if words_count[word] <= 0:
            continue
        used_words.append(word)
        words_count[word] -= 1
        find_combinations(idx + len(word), target, words_by_index, 
                          words_count, used_words)
        used_words.pop()
        words_count[word] += 1


words = input().split(", ")
target = input()

words_by_index = {}
words_count = {}

for word in words:
    if word in words_count:
        words_count[word] += 1
        continue
    
    words_count[word] = 1

    try:
        index = 0
        while True:
            index = target.index(word, index)
            if index not in words_by_index:
                words_by_index[index] = []
            words_by_index[index].append(word)
            index += len(word)
    except ValueError:
        pass

find_combinations(0, target, words_by_index, words_count, [])

