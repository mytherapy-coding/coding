import collections


def is_isogram0(string):
    count = collections.Counter(string.lower())
    for c in count.values():
        if c > 1:
            return False
    return True


def is_isogram1(string):
    count = collections.Counter(string.lower())
    return all(c == 1 for c in count.values())


def is_isogram2(string):
    count = collections.Counter(string.lower())
    res = []
    for c in count.values():
        if c != 1:
            res.append(c)

    return res == []


def is_isogram3(string):
    count = collections.Counter(string.lower())
    return [c for c in count.values() if c != 1] == []


def is_isogram4(string):
    return len(string) == len(set(string.lower()))


def test_isogram():
    tab: tuple[tuple[str, bool], ...] = (
        ("trnhssssssskioamf", False),
        ("", True),
        ("Dermatoglyphics", True),
        ("isIsogram", False),
        ("ABC", True),
    )
    for is_isorgam in is_isogram0, is_isogram1, is_isogram2, is_isogram3, is_isogram4:
        for string, expected in tab:
            result = is_isorgam(string)
            assert (
                result == expected
            ), f'failed on test {is_isorgam.__name__}("{string}")={result}, {expected=}'


test_isogram()
