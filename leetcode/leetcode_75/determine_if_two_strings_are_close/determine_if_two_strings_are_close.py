from collections import Counter


def closeStrings(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    counter1 = Counter(word1)
    counter2 = Counter(word2)
    return counter1.keys() == counter2.keys() and sorted(counter1.values()) == sorted(
        counter2.values()
    )


word1 = "abc"
word2 = "bca"
print(closeStrings(word1, word2))
word1 = "a"
word2 = "aa"
print((closeStrings(word1, word2)))
