import collections
import itertools
import operator
import functools


def longest_palindrome0(s):
    count = collections.Counter(s)
    res = 0
    found_odd = False
    for ch in count:
        if count[ch] % 2 == 0:
            res += count[ch]
        else:
            res += count[ch] - 1
            found_odd = True
    if found_odd:
        res += 1
    return res


def longest_palindrome1(s):
    count = collections.Counter(s)
    res = len(s)
    ending = 0
    for ch in count:
        ending += count[ch] % 2
    res -= ending
    if ending > 0:
        res += 1

    return res


def longest_palindrome2(s):
    count = collections.Counter(s)
    ending = sum(c % 2 for c in count.values())
    return len(s) - ending + (ending > 0)


def longest_palindrome3(s):
    count = collections.Counter(s)
    ending = sum(c % 2 for c in count.values())
    return len(s) - max(ending - 1, 0)


def longest_palindrome4(s):
    count = collections.Counter(s)
    ending = sum(itertools.islice((1 for c in count.values() if c % 2 == 1), 1, None))
    return len(s) - ending


def longest_palindrome5(s):
    res = set()
    for ch in s:
        if ch in res:
            res.remove(ch)
        else:
            res.add(ch)
    ending = len(res)
    return len(s) - max(ending - 1, 0)


def longest_palindrome6(s):
    res = set()
    for ch in s:
        res ^= {ch}
    ending = len(res)
    return len(s) - max(ending - 1, 0)


def longest_palindrome7(s):
    res = functools.reduce(operator.xor, ({ch} for ch in s), set())
    return len(s) - max(len(res) - 1, 0)


def run_test():

    tab = (
        ("aa", 2),
        ("abc", 1),
        ("aab", 3),
        ("", 0),
        ("bbb", 3),
        ("bbbaaa", 5),
    )
    funcs = (
        longest_palindrome0,
        longest_palindrome1,
        longest_palindrome2,
        longest_palindrome3,
        longest_palindrome4,
        longest_palindrome5,
        longest_palindrome6,
        longest_palindrome7,
    )

    for longest_palindrome in funcs:
        print(longest_palindrome.__name__)
        for s, expected in tab:
            print(longest_palindrome(s), expected)
        print()


run_test()
