import collections
import math


def string_divisor(s: str, t: str) -> bool:
    if not t:
        return True
    if len(s) % len(t) != 0:
        return False
    if not s.startswith(t):
        return False
    return s == t * (len(s) // len(t))


def gcdOfStrings0(str1: str, str2: str) -> str:
    res = ""
    for len_t in range(min(len(str1), len(str2)) + 1):
        if string_divisor(str1, (t := str1[0:len_t])) and string_divisor(str2, t):
            res = t

    return res


# reverse a loop to start from max prefix to 0, rangr(9, 0
# if and return
# join 13 and 14 (hint operator:=)
# list comprehension using the result 2 and collection.deque(maxlen = 1)
# lc from th task #1


def gcdOfStrings01(str1: str, str2: str) -> str:
    for len_t in range(min(len(str1), len(str2)), -1, -1):
        if string_divisor(str1, (t := str1[0:len_t])) and string_divisor(str2, t):
            return t
    return ""


def gcdOfStrings02(str1: str, str2: str) -> str:
    return next(
        t
        for len_t in range(min(len(str1), len(str2)), -1, -1)
        if string_divisor(str1, (t := str1[0:len_t])) and string_divisor(str2, t)
    )


def gcdOfStrings03(str1: str, str2: str) -> str:
    res = collections.deque(maxlen=1)
    for len_t in range(min(len(str1), len(str2)) + 1):
        if string_divisor(str1, (t := str1[0:len_t])) and string_divisor(str2, t):
            res.append(t)

    return res.pop()


def gcdOfStrings04(str1: str, str2: str) -> str:
    res = collections.deque(maxlen=1)
    res.extend(
        t
        for i in range(min(len(str1), len(str2)) + 1)
        if string_divisor(str1, (t := str1[:i])) and string_divisor(str2, t)
    )
    return res.pop()


def gcdOfStrings05(str1: str, str2: str) -> str:
    return collections.deque(
        (
            t
            for i in range(min(len(str1), len(str2)) + 1)
            if string_divisor(str1, (t := str1[:i])) and string_divisor(str2, t)
        ),
        maxlen=1,
    ).pop()


"""
1. find dividers for str1
    - find prefixes for str1
    - check what prefix is a divider
2. find dividers for str2
3. find common divider
4. find max common divider
"""


def gcdOfStrings1(str1: str, str2: str) -> str:
    def prefixes(s: str) -> list[str]:
        pre = []
        for i in range(len(s) + 1):
            pre.append(s[:i])
        return pre

    def str_dividers(s: str) -> list[str]:
        res = []
        for p in prefixes(s):
            if string_divisor(s, p):
                res.append(p)
        return res

    common_divisors = set(str_dividers(str1)) & set(str_dividers(str2))
    return max(common_divisors, key=len)


def gcdOfStrings2(str1: str, str2: str) -> str:
    def prefixes(s: str) -> list[str]:
        return [s[:i] for i in range(len(s) + 1)]

    def str_dividers(s: str) -> list[str]:
        return [p for p in prefixes(s) if string_divisor(s, p)]

    common_divisors = set(str_dividers(str1)) & set(str_dividers(str2))
    return max(common_divisors, key=len)


def gcdOfStrings3(str1: str, str2: str) -> str:
    def str_dividers(s: str) -> list[str]:
        return [s[:i] for i in range(len(s) + 1) if string_divisor(s, s[:i])]

    common_divisors = set(str_dividers(str1)) & set(str_dividers(str2))
    return max(common_divisors, key=len)


def gcdOfStrings4(str1: str, str2: str) -> str:
    def str_dividers(s: str) -> list[str]:
        return [s[:i] for i in range(len(s) + 1) if string_divisor(s, s[:i])]

    if len(str1) > len(str2):
        return gcdOfStrings4(str2, str1)

    common_divisors = [x for x in str_dividers(str1) if string_divisor(str2, x)]
    return max(common_divisors, key=len)


def gcdOfStrings5(str1: str, str2: str) -> str:
    t = str1[: math.gcd(len(str1), len(str2))]
    if string_divisor(str1, t) and string_divisor(str2, t):
        return t
    return ""


def gcdOfStrings6(str1: str, str2: str) -> str:
    t = str1[: math.gcd(len(str1), len(str2))]
    if string_divisor(str1, t) and string_divisor(str2, t):
        return t
    return ""


def test():
    tab = (
        ("ABCABC", "ABC", "ABC"),
        ("ABABAB", "ABAB", "AB"),
        ("AAAA", "AA", "AA"),
        ("a" * 15, "a" * 6, "aaa"),
        ("a" * 14 + "b", "a" * 6, ""),
    )
    for gcdOfStrings in (
        gcdOfStrings0,
        gcdOfStrings01,
        gcdOfStrings02,
        gcdOfStrings03,
        gcdOfStrings04,
        gcdOfStrings1,
        gcdOfStrings2,
        gcdOfStrings3,
        gcdOfStrings4,
        gcdOfStrings5,
    ):
        for str1, str2, expected in tab:
            result = gcdOfStrings(str1, str2)
            assert (
                result == expected
            ), f"{gcdOfStrings.__qualname__}({str1},{str2}) - {result =} {expected =}"


test()
