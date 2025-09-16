import math


def log2(n):
    return math.log2(n)


def find_x(nums: list, x) -> bool:
    if not nums:
        return False
    if len(nums) == 1:
        return nums[0] == x
    y = nums[len(nums) // 2]
    if y == x:
        return True
    if y > x:
        first_half = nums[: len(nums) // 2]
        return find_x(first_half, x)
    second_half = nums[len(nums) // 2 + 1 :]
    return find_x(second_half, x)


def find_x1(nums: list, x, beg: int, end: int) -> bool:
    if beg == end:
        return False
    if end == beg + 1:
        return nums[beg] == x
    mid = (beg + end) // 2
    y = nums[mid]
    if y == x:
        return True
    if y > x:
        return find_x1(nums, x, beg, mid)
    return find_x1(nums, x, mid + 1, end)


def find_x1(nums: list, x, beg: int, end: int) -> bool:
    if beg == end:
        return False
    if end == beg + 1:
        return nums[beg] == x
    mid = (beg + end) // 2
    y = nums[mid]
    if y == x:
        return True
    if y > x:
        return find_x1(nums, x, beg, mid)
    return find_x1(nums, x, mid + 1, end)


"""
def find_x2(nums: list,x, beg: int = 0, end: int = None) -> int:
    If end == None:
        end = len(nums)
    if beg == end:
        return -1
    if end == beg+1:
        return beg if nums[beg] == x else -1
    mid = (beg + end) // 2
    y = nums[mid]
    if y == x:
        return mid
    if y > x:
        return find_x2(nums, x, beg, mid)
    return find_x2(nums, x, mid +1 , end)


def log_it(find):
    def some_func(…):
        print(…)
        res = find(…)
        print(…)
        return res
    return some_func


log_find_x = log_it(find_x2)

nums = […]
x = …

print(find_x2(nums, x))
print(log_find_x(nums, x))
"""

"""
Задание:

Написать функцию, log_it, которая принимает один параметр, некую функцию, 
find, и возвращает новую функцию, которая делает три действия:
print(“start”)
вызов find(…)
print(“end”)


Сигнатура find и той функции, которую создает и возвращает log_it — идентичные,
обе функции принимают 4 параметра: nums, x, beg, end и обе должны возвращать тот же результат.
"""
