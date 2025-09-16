"""
GCD(a, b) - greatest common divider
c = GCD(a, b) - max divider
a%c == 0 and a%b == 0
a = c*k - 3*2
b = c*n - 3*3

let a < b

b = t*a + b%a
10 = t*3 + 10%3
12 = 4*3 + 12%3
16 = 5*3 + 16%3
19  = 6*3 + 19%3

(b%a)%c == 0

gcd(b%a, a) == gcd(a, b)

"""


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print(gcd(15, 5))
