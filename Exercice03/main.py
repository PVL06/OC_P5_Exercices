words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]


def number_vowel(word: str) -> int:
    number = 0
    for letter in word:
        if letter in "aeiouy":
            number += 1
    return number


result = [(word, number_vowel(word)) for word in words]
print(result)
