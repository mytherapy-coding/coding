from itertools import accumulate


def largestAltitude0(gain: list[int]) -> int:
    altitudes = [0]
    sum_altutude = 0
    for g in gain:
        sum_altutude += g
        altitudes.append(sum_altutude)
    return max(altitudes)


def largestAltitude1(gain: list[int]) -> int:
    def sum_alt():
        sum_altutude = 0
        yield sum_altutude
        for g in gain:
            sum_altutude += g
            yield sum_altutude

    return max(sum_alt())


def largestAltitude2(gain: list[int]) -> int:
    return max(accumulate(gain, initial=0))


def test():
    tab = (
        ([-5, 1, 5, 0, -7], 1),
        ([-4, -3, -2, -1, 4, 3, 2], 0),
    )

    funcs = (
        largestAltitude0,
        largestAltitude1,
        largestAltitude2,
    )
    for func in funcs:
        for gain, expected in tab:
            result = func(gain)
            assert result == expected, f'{func.__qualname__}({gain}: {result=}, {expected=}'


test()