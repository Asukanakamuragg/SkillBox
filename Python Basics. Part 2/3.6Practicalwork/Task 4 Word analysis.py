def is_palindrome(word: str) -> bool:
    word = word.lower().replace(" ", "")
    return word == word[::-1]

word = input("Введите слово: ")
if is_palindrome(word):
    print(f"{word} - Это палиндром")
else:
    print(f"{word} - Это не палиндром")
