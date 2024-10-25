# Объявите функцию single_root_words и напишите в ней параметры root_word и *other_words.

def single_root_words(root_word, *other_words):
# Создайте внутри функции пустой список same_words, который пополнится нужными словами.
    same_words = []
# При помощи цикла for переберите предполагаемо подходящие слова.
    for word in other_words:
        if root_word.lower().count(word.lower()) or word.lower().count(root_word.lower()):
            same_words.append(word)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
print(result1)
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result2)