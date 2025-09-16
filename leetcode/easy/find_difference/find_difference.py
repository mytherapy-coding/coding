import itertools
from collections import Counter


def findTheDifference(s: str, t: str) -> str:
    letters = list(t)
    for ch in s:
        letters.remove(ch)
    return str(letters)


def findTheDifference1(s: str, t: str) -> str:
    ordered_s = sorted(s)
    ordered_t = sorted(t)
    for a, b in zip(ordered_s, ordered_t):
        if a != b:
            return b
    return ordered_t[-1]


def findTheDifference2(s: str, t: str) -> str:
    ordered_s = sorted(s)
    ordered_t = sorted(t)
    return next((b for a, b in zip(ordered_s, ordered_t) if a != b), ordered_t[-1])


def findTheDifference3(s: str, t: str) -> str:
    ordered_s = sorted(s)
    ordered_t = sorted(t)
    return next(
        (b for a, b in zip(itertools.chain(ordered_s, [None]), ordered_t) if a != b)
    )


def findTheDifference4(s: str, t: str) -> str:
    ordered_s = sorted(s)
    ordered_t = sorted(t)
    return next((b for a, b in itertools.zip_longest(ordered_s, ordered_t) if a != b))


def findTheDifference5(s: str, t: str) -> str:
    count = collections.Counter(s)
    count1 = collections.Counter(t)
    value = count1 - count
    return next(c for c in value)


def findTheDifference6(s: str, t: str) -> str:
    return next(c for c in (collections.Counter(t) - collections.Counter(s)))


def findTheDifference7(s: str, t: str) -> str:
    count = collections.Counter(s)
    count1 = collections.Counter(t)
    value = count1 - count
    return list(value.keys())[list(value.values()).index(1)]


def findTheDifference8(s: str, t: str) -> str:
    count = collections.Counter(s)
    count1 = collections.Counter(t)
    value = count1 - count
    return next(value.elements())


def findTheDifference9(s: str, t: str) -> str:
    return next((Counter(t) - Counter(s)).elements())


def findTheDifference10(s: str, t: str) -> str:
    return ((Counter(t) - Counter(s)).most_common(1))[0][0]


print(findTheDifference10("hell", "hello"))
