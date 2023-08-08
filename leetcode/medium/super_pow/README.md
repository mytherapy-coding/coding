### Super Pow
### 
Your task is to calculate ab mod 1337 where a is a positive integer and b is an extremely large positive integer given in the form of an array.

### Solution

```py
def superPow(a: int, b: list[int]) -> int:
    M = 1337

    def powm(a, b):
        if b == 0:
            return 1
        if b == 1:
            return a % M
        if b % 2 == 0:
            return (powm(a, b // 2) ** 2) % M
        return (a * powm(a, b - 1)) % M
    
    res = 0
    for d in b:
        res *= 10
        res += d
    b = res

    return powm(a % M, b) % M

```
* Time Complexity: O(log b)
* Space Complexity: O(log b)

The solution is linear in time and space.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/super-pow/)


