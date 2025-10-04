def mySqrt(x: int) -> int:
    left = 0
    right = x + 1
    while left + 1 < right:
        mid = (left + right) // 2
        if mid * mid == x:
            return mid
        if mid * mid > x:
            right = mid
        else:
            left = mid
    return left


print(mySqrt(1))
