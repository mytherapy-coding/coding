
def isPerfectSquare0(num: int) -> bool:
    
    for y in range(num + 1):
        if y*y <= num:
            if y*y == num:
                return True
        else:
            break
    return False

# def isPerfectSquare(num: int) -> bool:


    
num = 16
print(isPerfectSquare0(num))
num = 15
print(isPerfectSquare0(num))


