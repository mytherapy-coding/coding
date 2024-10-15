# array, 20 elements, 0, step 10

# len(nums) = 20

nums = list(range(0, 200, 10))
print(type(nums))
print(len(nums))
print(nums)

# create a subarray from this array that will contain numbers from 100 to 150

ind = nums.index(100)
print(ind)
ind = nums.index(150)
print(ind)
sub_nums = nums[10:15]
print(sub_nums, f'nums[10:15]')

sub_nums2 = nums[11:16]
print(sub_nums2, f'nums[11:16]')

# Write a function that accepts a list of nums, a number x, and an integer k.
# It must find the index j of x in the list and return a sub array of size k that starts from the index j in nums.
print('_________')


def find_subarray(nums, x, k):
    j = nums.index(x)
    sub_array = nums[j:j+k]
    return sub_array


nums = list(range(0, 200, 10))
# [                    5              9   10
# [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120, 130, 140, 150, 160, 170, 180, 190]
x = 50
k = 5
print(find_subarray(nums, x, k))
