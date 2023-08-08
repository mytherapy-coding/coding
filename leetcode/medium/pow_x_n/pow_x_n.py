def myPow1(x: float, n: int) -> float:
    res = 1
    for _ in range(abs(n)):
        if n < 0:
            res *= 1 / x
        else:
            res *= x
    return res


def myPow2(x: float, n: int) -> float:
    res = 1
    if n < 0:
        x = 1 / x
    for _ in range(abs(n)):
        res *= x
    return res


def myPow3(x: float, n: int) -> float:
    res = 1
    for _ in range(abs(n)):
        res *= x
    return res if n >= 0 else 1 / res


def myPow4(x: float, n: int) -> float:
    if n < 0:
        return 1 / myPow4(x, -n)
    res = 1
    for _ in range(n):
        res *= x
    return res


def myPow5(x: float, n: int) -> float:  # log n linier in time, space log n
    if n == 1:
        return x
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow5(x, -n)
    y = myPow5(x, n // 2)
    if n % 2 == 0:
        return y * y
    return x * y * y


def myPow6(x: float, n: int) -> float:  # log n linier in time, space log n
    if n < 0:
        return 1/myPow6(x, -n)
    y = 1
    e = x
    while n > 0:
        if n % 2 == 1:
            y *= e
        e *= e
        n //= 2
    return y


def test():
    for myPow in myPow5, myPow6:
        print(myPow(5, 2))
        print(myPow(7, 3))
        print(myPow(0, 5))
        print(myPow(5, 0))
        print(myPow(2, 10))
        print(myPow(2, 20))
        print(myPow(2, 30))
        print(myPow(-2, 31))
        print(myPow(2.5, 2))
        print(myPow(2, -1))
        print(myPow(2, -2))
        print(myPow(2, -3))
        print(pow(2, -1))
        print(myPow(1 / 2, 3))


test()
