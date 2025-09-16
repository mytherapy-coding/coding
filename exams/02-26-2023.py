import math
import functools
import operator


# binom newton
def func(n):
    for i in range(n):
        print("O" * (n - i - 1) + "X" + "O" * (2 * i - 1) + "X" * (i > 0))


# func(5)


def func1(values):
    acc = 0
    for value in values:
        if value % 2 == 0:
            acc -= value
        else:
            acc += value
    return acc


def func2(nums):
    return sum(num**2 for num in nums)


def func3(nums):
    sorted_nums = sorted(nums)
    if len(nums) % 2 == 1:
        mean = nums[len(nums) // 2]
    else:
        mean = (nums[len(nums) // 2] + nums[len(nums) // 2 - 1]) / 2
    return sum(nums) / len(nums), mean


def H(n):
    total = 0
    for i in range(1, n + 1):
        total += 1 / i
    return total


"""
n = 50000000
print(H(n))
print(mymath.log(n))
print(H(n) - mymath.log(n))
"""


def factorial(n):  # 4
    prod = 1
    for i in range(n):
        prod *= i + 1
    return prod


def factorial1(n):
    prod = 1
    for i in range(1, n + 1):
        prod *= i
    return prod


def factorial2(n):
    return math.prod(range(1, n + 1))


def factorial3(n):
    return functools.reduce(operator.mul, range(1, n + 1), 1)


"""
print(factorial3(0))

print(list(range(1, 1)))

print(mymath.factorial(5))
"""


@functools.cache
def factorial4(n):
    if n == 0:
        return 1
    return factorial4(n - 1) * n


# print(factorial4(5))


def Comb(n, m):
    return math.factorial(n) // (math.factorial(m) * math.factorial(n - m))


def make_binom(N):
    c = [[0] * (n + 1) for n in range(N + 1)]
    for n in range(N + 1):
        for m in range(n + 1):
            c[n][m] = math.comb(n, m)
    return c


table = make_binom(10)
for row in table:
    print(row)


def make_binom1(N):
    return [[math.comb(n, m) for m in range(n + 1)] for n in range(N + 1)]


"""
(a+b)^2 = (a + b)*(a + b) = a^2 +2ab +b^2
(a+b)^3 = a^3 + 3a^2*b + 3ab^2 +b^3
C(n, m) = C(n-1, m) + C(n-1, m-1)
"""


@functools.cache
def C(n, m):
    # 0 <= m <= n
    if m == 0:
        return 1
    if m == n:
        return 1
    return C(n - 1, m) + C(n - 1, m - 1)


print(Comb(200, 100))
print(math.comb(200, 100))
print(C(200, 100))
print(make_binom1(5))
