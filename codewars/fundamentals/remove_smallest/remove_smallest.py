import operator
from collections.abc import Callable


def remove_smallest1(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    minimum = min(numbers)
    copy = numbers[:]
    copy.remove(minimum)
    return copy


def remove_smallest2(numbers: list[float]) -> list[float]:
    if len(numbers) == 0:
        return []
    minimum = min(numbers)
    copy = numbers[:]
    copy.remove(minimum)
    return copy


def remove_smallest3(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    copy = numbers[:]
    copy.remove(min(numbers))
    return copy


def remove_smallest4(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    min_num = min(numbers)
    min_index = numbers.index(min_num)
    return numbers[:min_index] + numbers[min_index + 1:]


def remove_smallest5(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    k = numbers.index(min_num)
    return numbers[:k] + numbers[k + 1:]


def remove_smallest6(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    min_num = numbers[0]
    k = 0
    for i, num in enumerate(numbers):
        if num < min_num:
            min_num = num
            k = i
    return numbers[:k] + numbers[k + 1:]


def remove_smallest7(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    min_num = numbers[0]
    k = 0
    for i, num in enumerate(numbers):
        if num < min_num:
            min_num = num
            k = i
    return numbers[:k] + numbers[k + 1:]


def remove_smallest8(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    k = 0
    for i, num in enumerate(numbers):
        if num < numbers[k]:
            k = i
    return numbers[:k] + numbers[k + 1:]


def remove_smallest9(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    res = []
    for i in range(len(numbers)):
        res.append((numbers[i], i))
    _, k = min(res)
    return numbers[:k] + numbers[k + 1:]


def remove_smallest10(numbers: list[float]) -> list[float]:
    if not numbers:
        return []
    _, k = min([(numbers[i], i) for i in range(len(numbers))])
    return numbers[:k] + numbers[k + 1:]


def remove_smallest11(numbers: list[float]) -> list[float]:
    _, k = min((numbers[i], i) for i in range(len(numbers))) if numbers else (0, 0)
    return numbers[:k] + numbers[k + 1:]


def remove_smallest12(numbers: list[float]) -> list[float]:
    _, k = min(((numbers[i], i) for i in range(len(numbers))), default=(0, 0))
    return numbers[:k] + numbers[k + 1:]


def remove_smallest13(numbers: list[float]) -> list[float]:
    _, k = min(((num, i) for i, num in enumerate(numbers)), default=(0, 0))
    return numbers[:k] + numbers[k + 1:]


def remove_smallest14(numbers: list[float]) -> list[float]:
    def get_key(t: tuple[int, float]) -> float:
        return t[1]

    k, _ = min(enumerate(numbers), default=(0, 0), key=get_key)
    return numbers[:k] + numbers[k + 1:]


def remove_smallest15(numbers: list[float]) -> list[float]:
    k, _ = min(enumerate(numbers), default=(0, 0), key=lambda t: t[1])
    return numbers[:k] + numbers[k + 1:]


def remove_smallest16(numbers: list[float]) -> list[float]:
    zipped = zip(numbers, range(len(numbers)))
    _, k = min(zipped, default=(0, 0))
    return numbers[:k] + numbers[k + 1:]


def remove_smallest17(numbers: list[float]) -> list[float]:
    _, k = min(zip(numbers, range(len(numbers))), default=(0, 0))
    return numbers[:k] + numbers[k + 1:]


def remove_smallest18(numbers: list[float]) -> list[float]:
    k: int = min(range(len(numbers)), key=lambda i: numbers[i], default=0)
    return numbers[:k] + numbers[k + 1:]


def remove_smallest19(numbers: list[float]) -> list[float]:
    k = min(range(len(numbers)), default=0, key=numbers.__getitem__)
    return numbers[:k] + numbers[k + 1:]


def remove_smallest20(numbers: list[float]) -> list[float]:
    k, _ = min(enumerate(numbers), default=(0, 0), key=operator.itemgetter(1))
    return numbers[:k] + numbers[k + 1:]


def tests_remove_smallest():
    tests: tuple[tuple[list[float], list[float]], ...] = (
        ([], []),
        ([7], []),
        ([6, 1], [6]),
        ([4, 7, 9, 9, 56], [7, 9, 9, 56]),
        ([30, 87, 5], [30, 87]),
        ([10, 65, 43], [65, 43]),
        ([100] * 1000 + [99], [100] * 1000),
        ([100] * 1000 + [101], [100] * 999 + [101]),
        (list(range(1000)), list(range(1, 1000))),
    )

    tested_funcs: tuple[Callable[[list[float]], list[float]], ...] = (
        remove_smallest1,
        remove_smallest2,
        remove_smallest3,
        remove_smallest4,
        remove_smallest5,
        remove_smallest6,
        remove_smallest7,
        remove_smallest8,
        remove_smallest9,
        remove_smallest10,
        remove_smallest11,
        remove_smallest12,
        remove_smallest13,
        remove_smallest14,
        remove_smallest15,
        remove_smallest16,
        remove_smallest17,
        remove_smallest18,
        remove_smallest19,
        remove_smallest20,
    )

    for f in tested_funcs:
        for numbers, expected in tests:
            computed = f(numbers)
            assert computed == expected, f'failed test on {f.__name__}({numbers=}): {computed}, {expected=}'

    print("end of tests")


tests_remove_smallest()
