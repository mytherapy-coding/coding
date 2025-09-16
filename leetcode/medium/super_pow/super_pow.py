def superPow1(a: int, b: list[int]) -> int:
    # b = int(''.join(str(d) for d in b))
    # [2, 5, 7]
    res = 0
    for d in b:
        res *= 10
        res += d
    b = res

    return pow(a, b) % 1337


def superPow2(a: int, b: list[int]) -> int:
    # b = int(''.join(str(d) for d in b))
    # [2, 5, 7]
    res = 0
    for d in b:
        res *= 10
        res += d
    b = res

    return pow(a % 1337, b) % 1337


def superPow3(a: int, b: list[int]) -> int:
    M = 1337

    def powm(a, b):
        if b == 0:
            return 1
        if b == 1:
            return a % M
        if b % 2 == 0:
            return (powm(a, b // 2) ** 2) % M
        return (a * powm(a, b - 1)) % M

    # b = int(''.join(str(d) for d in b))
    # [2, 5, 7]
    res = 0
    for d in b:
        res *= 10
        res += d
    b = res

    return powm(a % M, b) % M


"""
let a = 2^30 
let b = 10^2000
len(b) = 2000
log b = 2000 * log 10
a^b = (2^30)^(10^2000)
(x^y)^z = x^(y*z)
2^10 ~~ 1000 = 10^3
2^20 ~~ 10^6
2^30 ~~ 10^9
a^b = (10^9)^(10^2000) = 10^(10*10^2000) = 10^(10^2001) 
"""
print(superPow2(2, [1, 0]))
x = 1234567890987654321234567890987654
print(x % 1337)
print(x / 1337)
print(x // 1337)
print((x // 1337) * 1337)
print((x * x) % 1337)
print(len(str(x)))
# 10^34= ((10^3)^11)*10
print()
print((x * x) % 1337)
print(x % 1337)
print((210 * 210) % 1337)
print((x * x) % 1337)
print("--------")
print(superPow3(2, [1, 0]))

"""
(x*y) mod m = ((x mod m) * (y mod m)) mod m 
(x+y) mod m = ((x mod m) + (y mod m)) mod m 
(x^z) mod m = ((x mod m) ^ z) mod m
pow(a, b)%m = pow(a%m, b)%m
"""
