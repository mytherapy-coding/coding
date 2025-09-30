

def missingNumber1(nums: list[int]) -> int:
    n = len(nums)
    for x in range(n+1):
        if x not in nums:
            return x
       

def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    sorted_list = sorted(nums)
    prev_x = - 1
    for x in sorted_list:
        if x != prev_x + 1:
            return x - 1
        prev_x = x 
    return n
    

def missingNumber2(nums: list[int]) -> int:
    n = len(nums)
    sorted_list = sorted(nums)
    for i, x in enumerate(sorted_list):
        if i != x:
            return i
    return n


def missingNumber3(nums: list[int]) -> int:
    return next((i for i, x in enumerate(sorted(nums)) if i != x), len(nums))

def missingNumber4(nums: list[int]) -> int:
    return next(x for x in range(len(nums) + 1) if x not in nums)

print(missingNumber([0, 1, 2, 3]))
print(missingNumber1([0, 1, 2, 3]))
print(missingNumber2([0, 1, 2, 3]))      
print(missingNumber3([0, 1, 2, 3]))
print(missingNumber4([0, 1, 2, 3]))

# bisect 


# set


# list comprehension - n = len(nums)
#     for x in range(n+1):
#         if x not in nums:
#             return x


# next() any 

# sorted, 
# binary search my own loop devide by half and check where is a gap in left or right part - logn

# heap 


# quick sort 