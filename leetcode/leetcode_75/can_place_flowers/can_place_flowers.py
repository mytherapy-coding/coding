import itertools


def canPlaceFlowers0(flowerbed: list[int], n: int) -> bool:
    flowerbed = flowerbed[:]
    if n <= 0:
        return True
    if not flowerbed:
        return False
    if len(flowerbed) == 1:
        return flowerbed[0] == 0 and n <= 1

    count = 0
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        count += 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        count += 1
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
            flowerbed[i] = 1
            count += 1
    return count >= n


def canPlaceFlowers1(flowerbed: list[int], n: int) -> bool:
    flowerbed = flowerbed[:]
    if n <= 0:
        return True
    if not flowerbed:
        return False
    if len(flowerbed) == 1:
        return flowerbed[0] == 0 and n <= 1

    count = 0
    if flowerbed[:2] == [0, 0]:
        flowerbed[0] = 1
        count += 1
    if flowerbed[-2:] == [0, 0]:
        flowerbed[-1] = 1
        count += 1
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1 : i + 2] == [0, 0, 0]:
            flowerbed[i] = 1
            count += 1
    return count >= n


def canPlaceFlowers2(flowerbed: list[int], n: int) -> bool:
    flowerbed = flowerbed[:]
    if n <= 0:
        return True
    if not flowerbed:
        return False
    if len(flowerbed) == 1:
        return flowerbed[0] == 0 and n <= 1

    count = 0
    if flowerbed[0] == 0 and flowerbed[1] == 0:
        flowerbed[0] = 1
        count += 1
    if flowerbed[-1] == 0 and flowerbed[-2] == 0:
        flowerbed[-1] = 1
        count += 1
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i] == 0 and flowerbed[i + 1] == 0 and flowerbed[i - 1] == 0:
            flowerbed[i] = 1
            count += 1
    return count >= n


def canPlaceFlowers3(flowerbed: list[int], n: int) -> bool:
    flowerbed = flowerbed[:]
    if n <= 0:
        return True
    if not flowerbed:
        return False
    if len(flowerbed) == 1:
        return flowerbed[0] == 0 and n <= 1

    count = 0
    for i in range(len(flowerbed)):
        if flowerbed[i] == 0:
            if (i == 0 or flowerbed[i - 1] == 0) and (
                i == len(flowerbed) - 1 or flowerbed[i + 1] == 0
            ):
                flowerbed[i] = 1
                count += 1
    return count >= n


def canPlaceFlowers4(flowerbed: list[int], n: int) -> bool:
    flowerbed = [0] + flowerbed + [0]
    count = 0
    for i in range(1, len(flowerbed) - 1):
        if flowerbed[i - 1 : i + 2] == [0, 0, 0]:
            flowerbed[i] = 1
            count += 1
    return count >= n


def canPlaceFlowers5(flowerbed: list[int], n: int) -> bool:
    count = 0
    start = 0
    flowerbed = [0] + flowerbed + [0, 1]
    for end, flower in enumerate(flowerbed):
        if flower:
            length = end - start
            start = end + 1
            if length > 0:
                count += (length - 1) // 2
    return count >= n


def canPlaceFlowers6(flowerbed: list[int], n: int) -> bool:
    count = 0
    start = 0
    flowerbed = itertools.chain([0], flowerbed, [0, 1])
    for end, flower in enumerate(flowerbed):
        if flower:
            length = end - start
            start = end + 1
            if length > 0:
                count += (length - 1) // 2
    return count >= n


"""
[0, 0, 0, 0, 0] => 3
1, 0, 0, 0, 0, 0] => 2
[0, 0, 0, 0, 0, 1 => 2
1, 0, 0, 0, 0, 0, 1 => 2

[0, 0, 0, 0] => 2
1, 0, 0, 0, 0] => 2
[0, 0, 0, 0, 1 => 2
1, 0, 0, 0, 0, 1 => 1

[1, 0, 0, 0, 0, 0, 1] => 2
1, 0, 0, 0, 0, 1] => 1
[1, 0, 0, 0, 0, 1 => 1
1, 0, 0, 0, 1 => 1

[0, 0] => 1
1, 0, 0] => 1
[0, 0, 1 => 1
1, 0, 0, 1 => 0

"""

# intervals, no side effect, space complexity O(1)


def test():
    tab = (
        ([0] * 10, 4, True),
        ([], 0, True),
        ([], 1, False),
        ([0], 1, True),
        ([0], 0, True),
        ([0], 2, False),
        ([1], 1, False),
        ([1], 0, True),
        ([1, 0], 0, True),
        ([0, 1], 1, False),
        ([0, 0], 1, True),
    )

    funcs = (
        canPlaceFlowers0,
        canPlaceFlowers1,
        canPlaceFlowers2,
        canPlaceFlowers3,
        canPlaceFlowers4,
        canPlaceFlowers5,
        canPlaceFlowers6,
    )
    for func in funcs:
        for flowerbed, n, expected in tab:
            # print(flowerbed, n, expected)
            result = func(flowerbed, n)
            assert (
                result == expected
            ), f"{func.__qualname__}({flowerbed}, {n}): {result=}, {expected=}"


test()
