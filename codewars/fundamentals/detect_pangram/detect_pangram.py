import itertools
import string


def is_pangram1(s: str) -> bool:
    unique = {ch for ch in s.lower() if "a" <= ch <= "z"}
    return len(unique) == len(string.ascii_lowercase)


def is_pangram2(s: str) -> bool:
    unique = {ch for ch in s.lower() if ch.isalpha()}
    return unique == set(string.ascii_lowercase)


def is_pangram3(s: str) -> bool:
    return len({ch for ch in s.lower() if ch.isalpha()}) == len(string.ascii_lowercase)


def is_pangram4(s: str) -> bool:
    return set(string.ascii_lowercase) <= set(s.lower())


def is_pangram5(s: str) -> bool:
    return set(string.ascii_lowercase) - set(s.lower()) == set()


def is_pangram6(s: str) -> bool:
    return not bool(set(string.ascii_lowercase) - set(s.lower()))


def is_pangram7(s: str) -> bool:
    return not (set(string.ascii_lowercase) - set(s.lower()))


def is_pangram8(s: str) -> bool:
    uniq: set[str] = set(s.lower())
    res = []
    for ch in string.ascii_lowercase:
        res.append(ch in uniq)
    return all(res)


def is_pangram9(s: str) -> bool:
    uniq: set[str] = set(s.lower())
    return all(ch in uniq for ch in string.ascii_lowercase)


def is_pangram10(s: str) -> bool:
    uniq: set[str] = set()
    for ch in s:
        if ch.isalpha():
            uniq.add(ch.lower())
        if len(uniq) == len(string.ascii_lowercase):
            return True
    return False


def is_pangram11(s: str) -> bool:
    uniq: set[str] = set(string.ascii_lowercase)
    for ch in s:
        uniq.discard(ch.lower())
        if not uniq:
            return True
    return False


def is_pangram12(s: str) -> bool:
    uniq: set[str] = set()

    def f(_, ch):
        uniq.add(ch.lower()) if ch.isalpha() else ...
        return len(uniq) == len(string.ascii_lowercase)

    return any(itertools.accumulate(s, f, initial=0))


def is_pangram13(s: str) -> bool:
    uniq: set[str] = set(string.ascii_lowercase)

    def f(_, ch):
        uniq.discard(ch.lower())
        return uniq == set()

    return any(itertools.accumulate(s, f, initial=0))


def test_is_pangram():
    from collections.abc import Callable

    tab: tuple[tuple[str, bool], ...] = (
        ("", False),
        (" ", False),
        ("The quick, brown fox jumps over the lazy dog!", True),
        (string.ascii_lowercase, True),
        (string.ascii_uppercase, True),
        (string.ascii_letters, True),
        ("1bcdefghijklmnopqrstuvwxyz", False),
    )
    funcs: tuple[Callable[list[str], bool], ...] = (
        is_pangram1,
        is_pangram2,
        is_pangram3,
        is_pangram4,
        is_pangram5,
        is_pangram6,
        is_pangram7,
        is_pangram8,
        is_pangram9,
        is_pangram10,
        is_pangram11,
        is_pangram12,
        is_pangram13,
    )

    for f in funcs:
        for s, expected in tab:
            result = f(s)
            assert (
                result == expected
            ), f"test failed on {f.__name__}({s}, {expected=}, {result=}"


test_is_pangram()
