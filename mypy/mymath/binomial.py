import functools
import math


def Comb(n, m):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))


@functools.cache
def C(n, m):
    # 0 <= m <= n
    if m == 0:
        return 1
    if m == n:
        return 1
    return C(n - 1, m) + C(n - 1, m - 1)


def test_binom():
    funcs = [
        Comb,
        math.comb,
        C,
    ]
    for n, m in (200, 100), (200, 0), (200, 200), (200, 1):
        for f in funcs:
            print(f"{f.__name__}({n},{m})={f(n, m)}")


test_binom()


def make_binom(N):
    c = [[0] * (n + 1) for n in range(N + 1)]
    for n in range(N + 1):
        for m in range(n + 1):
            c[n][m] = math.comb(n, m)
    return c


def make_binom1(N):
    return [[math.comb(n, m) for m in range(n + 1)] for n in range(N + 1)]


"""
(a+b)^2 = (a + b)*(a + b) = a^2 +2ab +b^2
(a+b)^3 = a^3 + 3a^2*b + 3ab^2 +b^3
C(n, m) = C(n-1, m) + C(n-1, m-1)
"""


def test_make_binom():
    for mk_binom in make_binom, make_binom:
        for row in mk_binom(10):
            print(*row)


test_make_binom()
