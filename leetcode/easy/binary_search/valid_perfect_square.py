
def isPerfectSquare0(num: int) -> bool:
    
    for y in range(num + 1):
        if y*y > num:
            return False
        if y*y == num:
            return True
    return False

def isPerfectSquare(num: int) -> bool:
    low = 0
    high = num + 1
    while low < high:
        mid = (low + high)//2
        if mid*mid == num:
            return True
        if mid*mid > num:
            high = mid
        else:
            low = mid + 1
    return False



    
num = 16
print(isPerfectSquare(num))
num = 15
print(isPerfectSquare(num))


