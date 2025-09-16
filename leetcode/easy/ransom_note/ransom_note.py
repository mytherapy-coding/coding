import collections


def can_constract1(ransom_note: str, magazine: str) -> bool:
    count = collections.Counter(magazine)
    for ch in ransom_note:
        if count[ch] < 1:
            return False
        count[ch] -= 1
    return True


def can_constract2(ransom_note: str, magazine: str) -> bool:
    count = collections.Counter(magazine)
    count.subtract(ransom_note)
    return min(count.values()) >= 0


def can_constract3(ransom_note: str, magazine: str) -> bool:
    count = collections.Counter(magazine)
    count.subtract(ransom_note)
    return len(-count) == 0


def can_constract4(ransom_note: str, magazine: str) -> bool:
    magazine_count = collections.Counter(magazine)
    ransom_note_count = collections.Counter(ransom_note)
    return magazine_count >= ransom_note_count


def can_constract5(ransom_note: str, magazine: str) -> bool:
    i = j = 0
    sorted_ransom = sorted(ransom_note)
    sorted_magazine = sorted(magazine)
    while i < len(sorted_ransom) and j < len(sorted_magazine):
        if sorted_ransom[i] == sorted_magazine[j]:
            i += 1
            j += 1
        elif sorted_ransom[i] < sorted_magazine[j]:
            return False
        else:
            j += 1
    return i >= len(sorted_ransom)


def can_constract6(ransom_note: str, magazine: str) -> bool:
    sorted_ransom = sorted(ransom_note)
    sorted_magazine = sorted(magazine)
    i = j = 0
    while i < len(sorted_ransom) and j < len(sorted_magazine):
        if sorted_ransom[i] < sorted_magazine[j]:
            return False
        if sorted_ransom[i] == sorted_magazine[j]:
            i += 1
        j += 1
    return i >= len(sorted_ransom)


def can_constract7(ransom_note: str, magazine: str) -> bool:
    sorted_ransom = sorted(ransom_note)
    sorted_magazine = sorted(magazine)
    i = 0
    for j in range(len(sorted_magazine)):
        if i >= len(sorted_ransom):
            return True
        if sorted_ransom[i] < sorted_magazine[j]:
            return False
        if sorted_ransom[i] == sorted_magazine[j]:
            i += 1
    return i >= len(sorted_ransom)


def tests_can_constract():
    tab: tuple[tuple[str, str, bool], ...] = (
        ("aa", "aab", True),
        ("a", "ac", True),
        ("ab", "a", False),
        ("aaa", "a", False),
        ("asv", "v", False),
    )
    funcs: tuple[callable[[str, str], bool], ...] = (
        can_constract1,
        can_constract2,
        can_constract3,
        can_constract4,
        can_constract5,
        can_constract6,
        can_constract7,
    )
    for can_constract in funcs:
        for ransom_note, magazine, expected in tab:
            result = can_constract(ransom_note, magazine)
            assert (
                result == expected
            ), f"failed on {can_constract.__name__}({ransom_note=},{magazine=})={result}, {expected=}"


tests_can_constract()
