def guess(num):
        if num > 777:
            return -1
        if num < 777:
            return 1
        if num == 777:
            return 0



def guessNumber(n: int) -> int:
    low = 0
    high = n + 1
    while low < high:
        mid = (low + high)//2
        res = guess(mid)
        if res == 0:
            return mid
        if res < 0:
            high = mid
        else:
            low = mid

print(guessNumber(1000))
        
        
    
    