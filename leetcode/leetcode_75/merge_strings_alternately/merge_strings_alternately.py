import itertools


def mergeAlternately0(word1: str, word2: str) -> str:
    return "".join(
        itertools.chain.from_iterable(
            list(itertools.zip_longest(word1, word2, fillvalue=""))
        )
    )


def mergeAlternately1(word1: str, word2: str) -> str:
    return "".join(
        itertools.chain(*list(itertools.zip_longest(word1, word2, fillvalue="")))
    )


def mergeAlternately2(word1: str, word2: str) -> str:
    res = []
    i = 0
    j = 0
    while i < len(word1) and j < len(word2):
        res.append(word1[i])
        i += 1
        res.append(word2[j])
        j += 1
    if len(word1) > len(word2):
        res.append(word1[len(word2) :])
    else:
        res.append(word2[len(word1) :])

    return "".join(res)


def mergeAlternately3(word1: str, word2: str) -> str:
    res = []
    i = 0
    while i < min(len(word2), len(word1)):
        res.append(word1[i])
        res.append(word2[i])
        i += 1

    if len(word1) > len(word2):
        res.append(word1[len(word2) :])
    else:
        res.append(word2[len(word1) :])

    return "".join(res)


def mergeAlternately4(word1: str, word2: str) -> str:
    res = []
    for i in range(min(len(word2), len(word1))):
        res.append(word1[i])
        res.append(word2[i])
    if len(word1) > len(word2):
        res.append(word1[len(word2) :])
    else:
        res.append(word2[len(word1) :])

    return "".join(res)


def mergeAlternately5(word1: str, word2: str) -> str:
    res = []
    for ch1, ch2 in zip(word1, word2):
        res.append(ch1)
        res.append(ch2)
    if len(word1) > len(word2):
        res.append(word1[len(word2) :])
    else:
        res.append(word2[len(word1) :])

    return "".join(res)


def mergeAlternately6(word1: str, word2: str) -> str:
    res = []
    i = 0
    j = 0
    while i < len(word1) or j < len(word2):
        if i < len(word1):
            res.append(word1[i])
            i += 1
        if j < len(word2):
            res.append(word2[j])
            j += 1

    return "".join(res)


def mergeAlternately7(word1: str, word2: str) -> str:
    def merge():
        i = 0
        j = 0
        while i < len(word1) or j < len(word2):
            if i < len(word1):
                yield word1[i]
                i += 1
            if j < len(word2):
                yield word2[j]
                j += 1

    return "".join(merge())


def mergeAlternately8(word1: str, word2: str) -> str:
    res = []
    for ch1, ch2 in zip(word1, word2):
        res.append(ch1)
        res.append(ch2)
    res.append(word1[len(word2) :])
    res.append(word2[len(word1) :])
    return "".join(res)


def mergeAlternately9(word1: str, word2: str) -> str:
    if not word1:
        return word2
    if not word2:
        return word1
    return word1[0] + word2[0] + mergeAlternately9(word1[1:], word2[1:])


def mergeAlternately10(word1: str, word2: str) -> str:
    if not word1 or not word2:
        return word1 + word2

    return word1[0] + word2[0] + mergeAlternately10(word1[1:], word2[1:])


def mergeAlternately11(word1: str, word2: str) -> str:
    if not word1 or not word2:
        return word1 or word2

    return word1[0] + word2[0] + mergeAlternately11(word1[1:], word2[1:])


def mergeAlternately12(word1: str, word2: str) -> str:
    def merge(word1: str, word2: str) -> str:
        if not word1 or not word2:
            return word1 or word2

        return word1[0] + word2[0] + merge(word1[1:], word2[1:])

    return merge(word1, word2)


def mergeAlternately13(word1: str, word2: str) -> str:
    # alternatively merge word1[i:] and word2[j:]
    def merge(i: int, j: int) -> str:
        if i >= len(word1) or j >= len(word2):
            return word1[i:] or word2[j:]
        return word1[i] + word2[j] + merge(i + 1, j + 1)

    return merge(0, 0)


def mergeAlternately14(word1: str, word2: str) -> str:
    # alternatively merge word1[i:] and word2[j:]
    res = []

    def merge(i: int, j: int):
        if i >= len(word1) or j >= len(word2):
            res.append(word2[j:])
            res.append(word1[i:])
            return

        res.append(word1[i])
        res.append(word2[j])
        merge(i + 1, j + 1)

    merge(0, 0)
    return "".join(res)


def mergeAlternately15(word1: str, word2: str) -> str:
    # alternatively merge word1[i:] and word2[j:]
    res = ""

    def merge(i: int, j: int):
        nonlocal res
        if i >= len(word1) or j >= len(word2):
            res += word2[j:]
            res += word1[i:]
            return

        res += word1[i]
        res += word2[j]
        merge(i + 1, j + 1)

    merge(0, 0)
    return res


def test():

    tab = (
        ("abc", "pqr", "apbqcr"),
        ("ab", "pqrs", "apbqrs"),
        ("abcd", "pq", "apbqcd"),
    )

    funcs = (
        mergeAlternately0,
        mergeAlternately1,
        mergeAlternately2,
        mergeAlternately3,
        mergeAlternately4,
        mergeAlternately5,
        mergeAlternately6,
        mergeAlternately7,
        mergeAlternately8,
        mergeAlternately9,
        mergeAlternately10,
        mergeAlternately11,
        mergeAlternately12,
        mergeAlternately13,
        mergeAlternately14,
        mergeAlternately15,
    )

    for func in funcs:
        for word1, word2, expected in tab:
            result = func(word1, word2)
            assert (
                result == expected
            ), f"{func.__qualname__}({word1},{word2}): {result}, {expected=}"


test()
