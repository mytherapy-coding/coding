def add_binary1(a: int, b: int) -> str:
    return bin(a + b)[2:]


def add_binary2(a: int, b: int) -> str:
    return bin(a + b).removeprefix("0b")


def add_binary3(a: int, b: int) -> str:
    return f"{a + b:b}"


def add_binary4(a: int, b: int) -> str:
    c = a + b
    if c == 0:
        return "0"
    binary = ""
    while c > 0:
        binary += str(c % 2)
        c //= 2
    return binary[::-1]


def add_binary5(a: int, b: int) -> str:
    c = a + b
    if c == 0:
        return "0"
    binary = []
    while c > 0:
        binary.append(str(c % 2))
        c //= 2
    return "".join(reversed(binary))


def run_tests_for_add_binary():
    from collections.abc import Callable

    tab: list[tuple[int, int, str]] = [
        (0, 0, "0"),
        (1, 0, "1"),
        (6, 9, "1111"),
        (7, 9, "10000"),
    ]

    funcs: list[Callable[[int, int], str]] = [
        add_binary1,
        add_binary2,
        add_binary3,
        add_binary4,
        add_binary5,
    ]

    for f in funcs:
        for a, b, binary in tab:
            computed = f(a, b)
            print(f"{computed=}, {computed == binary}, {a}, {b}, {binary=}")


run_tests_for_add_binary()
