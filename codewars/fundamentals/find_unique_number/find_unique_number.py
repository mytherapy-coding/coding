import collections


def find_uniq1(arr: list[float]) -> float:
    count: dict[float, int] = dict()
    for e in arr:
        if e in count:
            count[e] += 1
        else:
            count[e] = 1

    for e in count.keys():
        if count[e] == 1:
            return e


def find_uniq2(arr: list[float]) -> float:
    count: dict[float, int] = dict()
    for e in arr:
        count[e] = count.get(e, 0) + 1

    for e in count.keys():
        if count[e] == 1:
            return e


def find_uniq3(arr: list[float]) -> float:
    count: dict[float, int] = collections.defaultdict(int)
    for e in arr:
        count[e] += 1

    for e in count.keys():
        if count[e] == 1:
            return e


def find_uniq4(arr: list[float]) -> float:
    count: dict[float, int] = collections.Counter(arr)

    for e in count.keys():
        if count[e] == 1:
            return e


def find_uniq5(arr: list[float]) -> float:
    count: collections.Counter[float] = collections.Counter(arr)
    res: list[float] = [e for e in count.keys() if count[e] == 1]
    return res[0]


def find_uniq6(arr: list[float]) -> float:
    count: collections.Counter[float] = collections.Counter(arr)
    return [e for e in count.keys() if count[e] == 1][0]


def find_uniq7(arr: list[float]) -> float:
    count: collections.Counter[float] = collections.Counter(arr)
    return next(e for e in count.keys() if count[e] == 1)


def find_uniq8(arr: list[float]) -> float:
    count: collections.Counter[float] = collections.Counter(arr)
    return count.most_common()[-1][0]


def find_uniq9(arr: list[float]) -> float:
    return collections.Counter(arr).most_common()[-1][0]


def find_uniq10(arr: list[float]) -> float:
    count: collections.Counter[float] = collections.Counter(arr)
    temp: dict[float, int] = {k: -v for k, v in count.items()}
    count = collections.Counter(temp)
    return count.most_common(1)[0][0]


def find_uniq11(arr: list[float]) -> float:
    return collections.Counter({k: -v for k, v in collections.Counter(arr).items()}).most_common(1)[0][0]


def find_uniq12(arr: list[float]) -> float:
    uniq: set[float] = set(arr)
    for e in uniq:
        if arr.count(e) == 1:
            return e


def find_uniq13(arr: list[float]) -> float:
    return [e for e in set(arr) if arr.count(e) == 1][0]


def find_uniq14(arr: list[float]) -> float:
    return [e for e in set(arr) if arr.count(e) == 1][0]


def find_uniq15(arr: list[float]) -> float:
    return next(e for e in set(arr) if arr.count(e) == 1)


def find_uniq16(arr: list[float]) -> float:
    ordered: list[float] = sorted(arr)
    if ordered[0] != ordered[1]:
        return ordered[0]
    return ordered[-1]


def find_uniq17(arr: list[float]) -> float:
    # O(n*log(n))
    ordered: list[float] = sorted(arr)
    return ordered[0] if ordered[0] != ordered[1] else ordered[-1]


def find_uniq18(arr: list[float]) -> float:
    skip: float
    if arr[0] != arr[1]:
        assert arr[0] == arr[2] or arr[1] == arr[2]
        skip = arr[2]
        # [100, 200, 100]
    else:
        assert arr[0] == arr[1]
        skip = arr[0]
        # [100, 100...]
    return [e for e in arr if e != skip][0]


def find_uniq19(arr: list[float]) -> float:
    skip: float = arr[2] if arr[0] != arr[1] else arr[0]
    return next(e for e in arr if e != skip)


def find_uniq20(arr: list[float]) -> float:
    skip: float = sorted(arr[:3])[1]
    return next(e for e in arr if e != skip)
    # [100, 200, 100] -> [100, 100, 200]
    # [200, 100, 100] -> [100, 100, 200]
    # [100, 200, 200] -> [100, 200, 200]
    # [200, 100, 200] -> [100, 200, 200]

    # [100, 100, 200] -> [100, 100, 200]
    # [200, 200, 100] -> [100, 200, 200]

    # [100, 100, 100] -> [100, 100, 100]


def test_find_uniq():
    from collections.abc import Callable

    tab: tuple[tuple[list[float], float], ...] = (
        ([100, 200, 200], 100),
        ([300, 300, 100], 100),
        ([1, 1, 1, 2, 1, 1], 2),
        ([0, 0, 0.55, 0, 0], 0.55),
        ([3, 10, 3, 3, 3], 10),

    )
    funcs: tuple[Callable[list[float], float], ...] = (
        find_uniq1,
        find_uniq2,
        find_uniq3,
        find_uniq4,
        find_uniq5,
        find_uniq6,
        find_uniq7,
        find_uniq8,
        find_uniq9,
        find_uniq10,
        find_uniq11,
        find_uniq12,
        find_uniq13,
        find_uniq14,
        find_uniq15,
        find_uniq16,
        find_uniq17,
        find_uniq18,
        find_uniq19,
        find_uniq20
    )

    for f in funcs:
        for arr, expected in tab:
            result = f(arr)
            assert result == expected, f'test failed on {f.__name__}({arr}), {expected=}, {result=}'


test_find_uniq()
