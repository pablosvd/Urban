def single_root_words(root_word, *other_words):
    same_words = []
    root_word = root_word.lower()
    other_words = list(other_words)
    lowercase_list = [s.lower() for s in other_words]
    for i in lowercase_list:
        if root_word in i:
            same_words.append(i)
        if i in root_word:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
