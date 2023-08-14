from typing import List

text = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"

# 1. Вивести в консоль довжину рядка (кількість символів)
length_characters = len(text)
print("Довжина рядна у символах:", length_characters)

# 2. Вивести в консоль довжину рядка (кількість слів)
words = text.split()
length_words = len(words)
print("Довжина рядка у словах:", length_words)


# 3. Розбити рядок на список окремих слів та замінити в кожному слові усі голосні літери іншим символом
vowels = "aeiouAEIOU"
words_replaced: list[str] = []
for word in words:
    replaced_word = ''.join(['&' if char in vowels else char for char in word])
    words_replaced.append(replaced_word)
    print("Рядок зі зміненими голосними літерами:".join(words_replaced))

# 4. Відновити рядок зі списку, зі вже заміненими словами
restored_text = ' '.join(words_replaced)
print("Відновлений рядок зі зміненими словами", restored_text)