"""
if n == 0 => 1
if n == 1 => 1
if n == 2 => 2
- 1+1
- 2
if n == 3 => 3
- 1+1+1
- 1+2
- 2+1
if n == 4 => 5
- 1+1+1+1
- 1+1+2
- 1+2+1
- 2+1+1
- 2+2
"""

"""
class Solution:
    def climbStairs(self, n: int) -> int:
        def fib(n: int) -> int:
            if n in (0, 1):
                return 1
            return fib(n-1) + fib(n-2)

        return fib(n)

"""
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        @cache
        def fib(n: int) -> int:
            if n in (0, 1):
                return 1
            return fib(n-1) + fib(n-2)

        return fib(n)
"""
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        d = {0:1, 1:1}
        def fib(n: int) -> int:
            if n in d:
                return d[n]
            d[n] = fib(n-1) + fib(n-2)
            return d[n]
            
        return fib(n)
"""
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        table = [1]*(n+1)
        for i in range(2, n+1):
            table[i] = table[i-1] + table[i-2]
        return table[n]
"""


class Solution:
    def climbStairs(self, n: int) -> int:
        f0 = f1 = 1
        for i in range(2, n + 1):
            f0, f1 = f1, f0 + f1

        return f1
