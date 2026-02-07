def findWordsContaining(words, x):
    result = []
    for i, w in enumerate(words):
        if x in w:
            result.append(i)
    return result


# ---- Manual Tests ----
print(findWordsContaining(["leet","code"], "e"))          # [0, 1]
print(findWordsContaining(["abc","bcd","aaaa","cbc"], "a"))  # [0, 2]
print(findWordsContaining(["abc","bcd","aaaa","cbc"], "z"))  # []
print(findWordsContaining([], "a"))                        # []
print(findWordsContaining(["x"], "x"))                     # [0]
print(findWordsContaining(["hello","world"], "l"))         # [0, 1]
print(findWordsContaining(["aaa","bbb","ccc"], "b"))       # [1]
