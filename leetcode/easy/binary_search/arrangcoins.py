import math

def arrangeCoins0(n: int) -> int:
    coins = 0
    for k in range(1, n + 2):
        coins += k
        if coins > n:
            return k - 1
        

def arrangeCoins1(n: int) -> int:
    for k in range(1, n + 2):
        coins = k*(k + 1)//2
        if coins > n:
            return k - 1
        
def arrangeCoins2(n: int) -> int:
    low = 1
    high = n + 1
    while low < high:
        mid = (low + high)//2 
        coins = mid*(1 + mid)//2 
        if coins == n:
            return mid
        if coins < n:
            low = mid  + 1
        else:
            high = mid 
    return low - 1
    
def arrangeCoins(n: int) -> int:
    return int((-1 + math.sqrt(1 + 8 * n)) / 2)



#### ####
# ## ### ##

# k(1 + k)/2 <= n < (k+1)(k+2)/2
n = 11
print(arrangeCoins(n))

#
##
###
####
#
