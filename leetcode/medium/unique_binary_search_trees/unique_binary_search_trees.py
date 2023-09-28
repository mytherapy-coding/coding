from functools import cache


def numTrees(n: int) -> int:
    def nodes(n: int) -> int:
        if n == 1:
            return 1
        if n == 0:
            return 1
        total = 0
        for k in range(n):
            total += nodes(k) * nodes(n - k - 1)
        return total

    return nodes(n)


def numTrees1(n: int) -> int:
    @cache
    def nodes(n: int) -> int:
        if n == 0:
            return 1
        return sum((nodes(k) * nodes(n - k - 1)) for k in range(n))

    return nodes(n)


def numTrees2(n: int) -> int:
    d = {}

    def nodes(n: int) -> int:
        if n in d:
            return d[n]
        if n == 0:
            return 1
        d[n] = sum((nodes(k) * nodes(n - k - 1)) for k in range(n))
        return d[n]

    return nodes(n)


def numTrees3(n: int) -> int:
    d = {0: 1}

    def nodes(n: int) -> int:
        if n not in d:
            d[n] = sum((nodes(k) * nodes(n - k - 1)) for k in range(n))
        return d[n]

    return nodes(n)


print(numTrees3(3))
