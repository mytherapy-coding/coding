
def missingNumber1(nums: list[int]) -> int:
    n = len(nums)
    for x in range(n+1):
        if x not in nums:
            return x
       

print(missingNumber1([0, 1, 2, 3]))

def missingNumber(nums: list[int]) -> int:
    n = len(nums)
    sorted_list = sorted(nums)
    prev_x = - 1
    for x in sorted_list:
        if x != prev_x + 1:
            return x - 1
        prev_x = x 
    return n
    
        
print(missingNumber([0, 1, 2, 3]))


def missingNumber2(nums: list[int]) -> int:
    n = len(nums)
    sorted_list = sorted(nums)
    for i, x in enumerate(sorted_list):
        if i != x:
            return i
    return n
print(missingNumber([0, 1, 2, 3]))



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