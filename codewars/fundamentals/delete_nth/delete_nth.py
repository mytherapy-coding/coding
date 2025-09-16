import collections
import functools
import itertools


def delete_nth1(order: list[float], max_e: int) -> list[float]:
    res: list[float] = []
    for e in order:
        if res.count(e) < max_e:
            res.append(e)

    return res


def delete_nth2(order: list[float], max_e: int) -> list[float]:
    res: list[float] = []
    for i, e in enumerate(order):
        if order[:i].count(e) < max_e:
            res.append(e)

    return res


def delete_nth3(order: list[float], max_e: int) -> list[float]:
    return [e for i, e in enumerate(order) if order[:i].count(e) < max_e]


def delete_nth4(order: list[float], max_e: int) -> list[float]:
    count: collections.Counter[float] = collections.Counter()
    res: list[float] = []
    for e in order:
        if count[e] < max_e:
            count[e] += 1
            res.append(e)

    return res


def delete_nth5(order: list[float], max_e: int) -> list[float]:
    count = {}
    res: list[float] = []
    for e in order:
        if count.get(e, 0) < max_e:
            count[e] = count.get(e, 0) + 1
            res.append(e)

    return res


def delete_nth6(order: list[float], max_e: int) -> list[float]:
    count = collections.defaultdict(int)
    res: list[float] = []
    for e in order:
        if count[e] < max_e:
            count[e] += 1
            res.append(e)

    return res


def delete_nth7(order: list[float], max_e: int) -> list[float]:
    res = order[::-1]
    for e in order:
        while res.count(e) > max_e:
            res.remove(e)

    return res[::-1]


def delete_nth8(order: list[float], max_e: int) -> list[float]:
    res = order[:]
    for i in reversed(range(len(order))):
        if res.count(order[i]) > max_e:
            del res[i]

    return res


def delete_nth9(order: list[float], max_e: int) -> list[float]:
    count: collections.Counter[float] = collections.Counter()

    def f(res: list[float], e: float) -> list[float]:
        count[e] += 1
        res.append(e) if count[e] <= max_e else ...
        return res

    return list(functools.reduce(f, order, []))


def delete_nth10(order: list[float], max_e: int) -> list[float]:
    count: collections.Counter[float] = collections.Counter()
    return [e for e in order if count.update([e]) or count[e] <= max_e]


def delete_nth11(order: list[float], max_e: int) -> list[float]:
    count: collections.Counter[float] = collections.Counter()
    res = []
    for e in order:
        count.update([e])
        if count[e] <= max_e:
            res.append(e)

    return res


def test_delete_nth():
    from collections.abc import Callable

    tab: tuple[tuple[list[float], int, list[float]], ...] = (
        ([], 0, []),
        ([], 10, []),
        ([4], 1, [4]),
        ([6], 0, []),
        ([6] * 100, 0, []),
        ([6] * 100, 1, [6]),
        ([6] * 100, 99, [6] * 99),
        ([6] * 100, 100, [6] * 100),
        ([6] * 100, 200, [6] * 100),
        (
            [1, 1, 3, 3, 7, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1],
            3,
            [1, 1, 3, 3, 7, 2, 2, 2, 1],
        ),
        ([1, 2, 3, 1, 2, 1, 2, 3], 2, [1, 2, 3, 1, 2, 3]),
        ([20, 20, 20, 20], 1, [20]),
        ([20, 37, 20, 21], 1, [20, 37, 21]),
        (list(range(10)), 1, list(range(10))),
        (list(range(10)) * 5, 1, list(range(10))),
        (sorted(list(range(10)) * 5), 1, list(range(10))),
        (
            sorted(list(range(10)) * 5),
            2,
            list(itertools.chain(*[[i, i] for i in range(10)])),
        ),
        (sorted(list(range(10)) * 5), 2, [x // 2 for x in range(20)]),
    )
    funcs: tuple[Callable[list[float], float], ...] = (
        delete_nth1,
        delete_nth2,
        delete_nth3,
        delete_nth4,
        delete_nth5,
        delete_nth6,
        delete_nth7,
        delete_nth8,
        delete_nth9,
        delete_nth10,
        delete_nth11,
    )

    for f in funcs:
        for order, max_e, expected in tab:
            result = f(order, max_e)
            assert (
                result == expected
            ), f"test failed on {f.__name__}({order}, {max_e}), {expected=}, {result=}"


test_delete_nth()
