def expanded_form1(num: int) -> str:
    res: list[str] = []
    k = len(str(num)) - 1
    for digit in str(num):
        if digit != '0':
            res.append(digit + '0' * k)
        k = k - 1

    return ' + '.join(res)


def expanded_form2(num: int) -> str:
    res: list[str] = []
    indexes = range(len(str(num)) - 1, -1, -1)
    for k, digit in zip(indexes, str(num)):
        if digit != '0':
            res.append(digit + '0' * k)

    return ' + '.join(res)


def expanded_form3(num: int) -> str:
    indexes = range(len(str(num)) - 1, -1, -1)
    res: list[str] = [digit + '0' * k for k, digit in zip(indexes, str(num)) if digit != '0']

    return ' + '.join(res)


def expanded_form4(num: int) -> str:
    return ' + '.join(digit + '0' * k for k, digit in zip(range(len(str(num)) - 1, -1, -1), str(num)) if digit != '0')


def expanded_form5(num: int) -> str:
    res: list[str] = []
    digits = str(num)
    for i in range(len(digits)):
        digit = digits[i]
        if digit != '0':
            res.append(digit + '0' * (len(digits) - i - 1))

    return ' + '.join(res)


def expanded_form6(num: int) -> str:
    res: list[str] = []
    digits = str(num)
    for i, digit in enumerate(digits):
        if digit != '0':
            res.append(digit + '0' * (len(digits) - i - 1))

    return ' + '.join(res)


def expanded_form7(num: int) -> str:
    digits = str(num)

    return ' + '.join(digit + '0' * (len(digits) - i - 1) for i, digit in enumerate(digits) if digit != '0')


def expanded_form8(num: int) -> str:
    res: list[str] = []
    k = 0
    for digit in reversed(str(num)):
        if digit != '0':
            res.append(digit + '0' * k)
        k += 1

    return ' + '.join(reversed(res))


def expanded_form9(num: int) -> str:
    res: list[str] = []
    for k, digit in enumerate(reversed(str(num))):
        if digit != '0':
            res.append(digit + '0' * k)

    return ' + '.join(reversed(res))


def expanded_form10(num: int) -> str:
    return ' + '.join(reversed([digit + '0' * k for k, digit in enumerate(reversed(str(num))) if digit != '0']))


def expanded_form11(num: int) -> str:
    digits: list[int] = []
    while num > 0:
        digit = num % 10
        num //= 10
        digits.append(digit)
    k = 0
    res: list[str] = []
    for digit in digits:
        if digit != 0:
            res.append(str(digit) + '0' * k)
        k += 1
    return ' + '.join(reversed(res))


def expanded_form12(num: int) -> str:
    k = 0
    res: list[str] = []
    while num > 0:
        digit = num % 10
        num //= 10
        if digit != 0:
            res.append(str(digit) + '0' * k)
        k += 1

    return ' + '.join(reversed(res))


def expanded_form13(num: int) -> str:
    e = 1
    res: list[str] = []
    while num > 0:
        digit = num % 10
        num //= 10
        if digit != 0:
            # e = 10**k
            res.append(str(digit * e))
        e *= 10

    return ' + '.join(reversed(res))


def expanded_form14(num: int) -> str:
    def gen(num: int):
        e = 1
        while num > 0:
            digit = num % 10
            num //= 10
            if digit != 0:
                # e = 10**k
                yield str(digit * e)
            e *= 10

    return ' + '.join(reversed(list(gen(num))))


def expanded_form15(num: int) -> str:
    def gen(num: int):
        e = 1
        while num > 0:
            digit = num % 10
            num //= 10
            yield digit * e
            e *= 10

    return ' + '.join(reversed([str(x) for x in gen(num) if x != 0]))


def tests_expanded_form():
    from collections.abc import Callable

    tab: tuple[tuple[int, str], ...] = (
        (0, ''),
        (1, '1'),
        (10, '10'),
        (5, '5'),
        (10**1000, '1' + '0'*1000),
        (10**1000 - 1, ' + '.join('9' + '0' * k for k in range(999, -1, -1)))
    )
    funcs: tuple[Callable[[int], str], ...] = (
        expanded_form1,
        expanded_form2,
        expanded_form3,
        expanded_form4,
        expanded_form5,
        expanded_form6,
        expanded_form7,
        expanded_form8,
        expanded_form9,
        expanded_form10,
        expanded_form11,
        expanded_form12,
        expanded_form13,
        expanded_form14,
        expanded_form15,
    )

    for f in funcs:
        for num, expected in tab:
            result = f(num)
            assert result == expected, f'test failed on {f.__name__}({num}), {expected=}, {result=}'


tests_expanded_form()
