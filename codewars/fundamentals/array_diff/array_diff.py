def array_diff0(a: list, b: list) -> list:
    c = a[:]
    for x in b:
        for i in range(a.count(x)):
            c.remove(x)

    return c


def array_diff1(a: list, b: list) -> list:
    c = []
    for x in a:
        if x not in b:
            c.append(x)

    return c


def array_diff2(a: list, b: list) -> list:
    b = set(b)
    c = []
    for x in a:
        if x not in b:
            c.append(x)

    return c


def array_diff3(a: list, b: list) -> list:
    b = set(b)
    return [x for x in a if x not in b]


tab = (
    ([], [], []),
    ([], [1, 2], []),
    ([5, 5, 7], [], [5, 5, 7]),
    ([10, 20], [], [10, 20]),
    ([3, 7, 6, 7], [7, 2], [3, 6]),
    ([9, 9, 7], [7], [9, 9]),
)

for f in array_diff0, array_diff1, array_diff2, array_diff3:
    for a, b, c in tab:
        assert f(a, b) == c, f"failed test on {f.__name__}({a}, {b}), expected {c}"
