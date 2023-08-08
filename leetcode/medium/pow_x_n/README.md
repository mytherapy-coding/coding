### Pow(x, n)

### 

Implement pow(x, n), which calculates x raised to the power n (i.e., xn).

### Solution

```py
def myPow(x: float, n: int) -> float: 
    if n == 1:
        return x
    if n == 0:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    y = myPow(x, n // 2)
    if n % 2 == 0:
        return y * y
    return x * y * y

```
* Time Complexity: O(log n)
* Space Complexity: O(log n)

The solution is linear in time and space.

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/powx-n/)


































