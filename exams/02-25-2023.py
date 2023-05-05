import math

def f0(a, b):
    return a * b


def f1(n):
    for _ in range(n):
        print(n * '#')


def f2(n):
    for i in range(1, n + 1):
        print("#" * i)


def f3(n):
    for i in range(n):
        print(" " * i + "#")


def f4(n):
    for i in range(n):
        print("O" * i + "#" + "O" * (n - i - 1))


def f5(n):
    for i in range(n - 1, -1, -1):
        print("O" * i + "#")


def f6(n):
    for i in range(n):
        print("O" * i + "#" * (i + 1))


def f7(n):
    res = 0
    for i in range(1, n + 1):
        res += i ** 2
    return res

def f8(n):
    return sum(i**2 for i in range(1, n+1))


def f9(x, k):
    res = 0
    sign = 1
    for i in range(1, 2*k, 2):
        res += x**i/i*sign
        sign = -sign
    return res


def f10(k):
    res = 0
    sign = 1
    for i in range(1, 2*k, 2):
        res += 1/i*sign
        sign = -sign
    return res*4

# x / 1 - x ^ 3 / 3 + x ^ 5 / 5 - x ^ 7 / 7 + …

print(f9(1, 100000))

print(math.atan(1))
print(math.pi/4)
print(f10(100000))