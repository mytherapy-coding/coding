def string_ends_with1(string: str, ending: str) -> bool:
    return string.endswith(ending)


def string_ends_with2(string: str, ending: str) -> bool:
    return string[len(string) - len(ending) :] == ending


def string_ends_with3(string: str, ending: str) -> bool:
    if len(string) < len(ending):
        return False

    for i in range(1, len(ending) + 1):
        if ending[-i] != string[-i]:
            return False

    return True


def string_ends_with4(string: str, ending: str) -> bool:
    if len(string) < len(ending):
        return False

    matched = []
    for i in range(1, len(ending) + 1):
        if ending[-i] == string[-i]:
            matched.append(i)

    return len(matched) == len(ending)


def string_ends_with5(string: str, ending: str) -> bool:
    if len(string) < len(ending):
        return False

    matched = [i for i in range(len(ending)) if ending[i] == string[-len(ending) + i]]

    return len(matched) == len(ending)


def string_ends_with6(string: str, ending: str) -> bool:
    if len(string) < len(ending):
        return False

    return all(ending[i] == string[-len(ending) + i] for i in range(len(ending)))


def run_tests():
    tab: list[tuple[str, str, bool]] = [
        ("", "lost", False),
        (";", "", True),
        ("", "", True),
        ("forever", "", True),
        ("forever", "r", True),
        ("forever", "e", False),
        ("forever", "ever", True),
        ("forever", "forever", True),
        ("forever", "foreverr", False),
        ("endswith", "end", False),
        ("love you", "love", False),
        ("timeshare", "share", True),
        ("unrealistic", "realistic", True),
        ("copay", "pay", True),
        ("a" * 1000000, "a" * 900000, True),
        ("a" * 1000000, "a" * 900000 + "b", False),
        ("a" * 1000000, "b" + "a" * 900000, False),
    ]

    tested_funcs = [
        string_ends_with1,
        string_ends_with2,
        string_ends_with3,
        string_ends_with4,
        string_ends_with5,
        string_ends_with6,
    ]
    for f in tested_funcs:
        for string, ending, expected in tab:
            computed = f(string, ending)
            assert (
                computed == expected
            ), f"failed test on {f.__name__}({string=}, {ending=})={computed}, but {expected=}"


run_tests()
