import string


def to_jaden_case1(s: str) -> str:
    return string.capwords(s, " ")


def to_jaden_case2(s: str) -> str:
    res: list[str] = []
    words = s.split(" ")
    for w in words:
        res.append(w.capitalize())

    return " ".join(res)


def to_jaden_case3(s: str) -> str:
    return " ".join(w.capitalize() for w in s.split(" "))


def to_jaden_case4(s: str) -> str:
    res: list[str] = []
    for c in s:
        if c.isspace():
            res.append(c)
        elif not res or res[-1].isspace():
            res.append(c.upper())
        else:
            res.append(c.lower())

    return "".join(res)


def to_jaden_case5(s: str) -> str:
    res: list[str] = []
    for i, c in enumerate(s):
        if c.isspace():
            res.append(c)
        elif i == 0 or s[i - 1].isspace():
            res.append(c.upper())
        else:
            res.append(c.lower())

    return "".join(res)


def to_jaden_case6(s: str) -> str:
    res: list[str] = []
    for i, c in enumerate(s):
        if c.isspace():
            z = c
        elif i == 0 or s[i - 1].isspace():
            z = c.upper()
        else:
            z = c.lower()

        res.append(z)

    return "".join(res)


def to_jaden_case7(s: str) -> str:
    res: list[str] = []
    for i, c in enumerate(s):
        z = (
            c
            if c.isspace()
            else c.upper() if i == 0 or s[i - 1].isspace() else c.lower()
        )
        res.append(z)

    return "".join(res)


def to_jaden_case8(s: str) -> str:
    res: list[str] = []
    for i, c in enumerate(s):
        res.append(
            c
            if c.isspace()
            else c.upper() if i == 0 or s[i - 1].isspace() else c.lower()
        )

    return "".join(res)


def to_jaden_case9(s: str) -> str:
    res: list[str] = [
        c if c.isspace() else c.upper() if i == 0 or s[i - 1].isspace() else c.lower()
        for i, c in enumerate(s)
    ]
    return "".join(res)


def to_jaden_case10(s: str) -> str:
    return "".join(
        c if c.isspace() else c.upper() if i == 0 or s[i - 1].isspace() else c.lower()
        for i, c in enumerate(s)
    )


def to_jaden_case11(s: str) -> str:
    res = ""
    for w in s.split(" "):
        res += w.capitalize()
        res += " "

    return res[:-1]


def to_jaden_case12(s: str) -> str:
    res = ""
    for w in s.split(" "):
        res += w.capitalize() + " "

    return res[:-1]


def test_to_jaden_case():
    from collections.abc import Callable

    tab: tuple[tuple[str, str], ...] = (
        ("", ""),
        (" ", " "),
        ("   ", "   "),
        ("hello", "Hello"),
        ("hello world", "Hello World"),
        ("?! 6/*", "?! 6/*"),
        ("  hello  world  ", "  Hello  World  "),
        (" love you", " Love You"),
    )

    funcs: tuple[Callable[[str], str], ...] = (
        to_jaden_case1,
        to_jaden_case2,
        to_jaden_case3,
        to_jaden_case4,
        to_jaden_case5,
        to_jaden_case6,
        to_jaden_case7,
        to_jaden_case8,
        to_jaden_case9,
        to_jaden_case10,
        to_jaden_case11,
        to_jaden_case12,
    )
    for f in funcs:
        for s, expected in tab:
            result = f(s)
            assert (
                result == expected
            ), f'failed test on {f.__name__}("{s}"): {result=}, {expected=}'


def perftest_to_jaden_case():
    from collections.abc import Callable
    import timeit, math

    n = 4_000_000
    tab: tuple[tuple[str, int], ...] = (
        ("b" * n, 1),
        (" " * n, 1),
        ("b " * (n // 2), 1),
        ("bbbb " * (n // 5), 1),
        (("b" * int(math.sqrt(n)) + " ") * int(math.sqrt(n)), 1),
    )
    funcs: tuple[Callable[[str], str], ...] = (
        to_jaden_case1,
        to_jaden_case2,
        to_jaden_case3,
        to_jaden_case4,
        to_jaden_case5,
        to_jaden_case6,
        to_jaden_case7,
        to_jaden_case8,
        to_jaden_case9,
        to_jaden_case10,
        to_jaden_case11,
        to_jaden_case12,
    )
    for i, (s, number) in enumerate(tab):
        print(
            f"test: {i}, {number=:}: {len(s)=:,}, {s[:10]=}, #words: {len(s.split()):,}, #spaces: {sum(int(c.isspace()) for c in s):,}, longest word: {max((len(w) for w in s.split()), default=0):,}"
        )
        for f in funcs:
            t = timeit.timeit(
                stmt=f"{f.__name__}(s)", number=number, globals={f.__name__: f, "s": s}
            )
            print(f"{f.__name__}: {t:.3f}")

        print()


test_to_jaden_case()

perftest_to_jaden_case()

#####


def to_jaden_case5(s: str) -> str:
    res: list[str] = []  # O(1)
    # n * O(1) = O(n)
    for i, c in enumerate(s):  # n,  n = len(s)
        # O(1)
        if c.isspace():  # O(1)
            res.append(c)  # O(1)
        elif i == 0 or s[i - 1].isspace():  # O(1) + O(1)
            res.append(c.upper())  # O(1) + O(1)
        else:
            res.append(c.lower())  # O(1) + O(1)

    return "".join(res)  # O(n)

    # O(1) + O(n) + O(n) = O(n)
