from collections.abc import Iterable

'''
Do not use any loop statements (for or while), do not use any mutable data structure
(like list, set, dict, deque, Counter, etc), do not use assignment or update operators
(like =, +=, *=, etc).

You may use generator expression (with for expression) if needed.

Write a function print_stars(k: int) that prints k lines each line is 'hello':

k = 3

hello
hello
hello


Write a function that given integer k, prints k lines:

***
**
*

Write a function that given k, prints:

1 2 3
1 2
1

Write a function that given strings s, compute and return its reverse. Do not use standard functions like reverse or reverse slicing [::-1].

Write a function that given a tuple (containing numbers), compute its sum. Don’t use the standard functions, like sum, reduce, etc).

Write a function that given a tuple (containing number), compute a new tuple that doubles each number in the given tuple.

Input: (10, 20, 15)
Output: (20, 40, 30)

Write a function that dips each element in the given tuple. Do not use comprehension or any library like collection.

Input: (10, 20, 15)
Output: (10, 10, 20, 20, 15, 15)
'''


def print_stars(k: int):
    if k <= 0:
        return
    print_stars(k - 1)
    print('Hello')


def print_stars1(k: int):
    for _ in range(k):
        print("hello")


def print_k(k: int):
    if k == 0:
        return
    print('*' * k)
    print_k(k - 1)


def print_k1(k: int):
    if k == 0:
        return
    print_k1(k - 1)
    print('*' * k)


def print_k2(k: int):
    if k == 0:
        return
    print('x' * k)
    print_k2(k - 1)
    print('*' * k)


def print_k3(k: int):
    if k == 0:
        return
    print('# ' * (k // 2) + "#")
    print_k3(k - 1)
    print('* ' * (k // 2) + "*")


def print_123(k: int):
    if k == 0:
        return
    print(" ".join(str(i) for i in range(1, k + 1)))
    print_123(k - 1)


def print_1234(k: int):
    if k == 0:
        return
    print(" ".join(map(str, range(1, k + 1))))
    print_1234(k - 1)


def print_12345(k: int):
    if k == 0:
        return
    print(*list(range(1, k + 1)))
    print_12345(k - 1)


'''
Write a function that given strings s, compute and return its reverse. 
Do not use standard functions like reverse or reverse slicing [::-1].
'''


def reverse_s(s):
    return reverse_s(s[1:]) + s[0] if s else ''


'''
Write a function that given a tuple (containing numbers), compute its sum. 
Don’t use the standard functions, like sum, reduce, etc).
'''


def compute_sum(nums: list[int]) -> int:
    if not nums:
        return 0
    return compute_sum(nums[1:]) + nums[0]


def my_sum(*nums):
    return compute_sum(nums[1:]) + nums[0] if nums else 0


'''
Write a function that given a tuple (containing number), 
compute a new tuple that doubles each number in the given tuple.

Input: (10, 20, 15)
Output: (20, 40, 30)
'''


def double(nums: list[int]) -> list:
    if not nums:
        return []
    return [nums[0] * 2] + double(nums[1:])


print(double([10, 20, 30]))

'''
Write a function that duplicates each element in the given tuple. 
Do not use comprehension or any library like collection.

Input: (10, 20, 15)
Output: (10, 10, 20, 20, 15, 15)
'''


def dups(nums: list[int]) -> list:
    if not nums:
        return []
    return [nums[0], nums[0]] + dups(nums[1:])


print(dups([10, 20, 30]))

'''
Посчитать факториал k.

Посчитать сумму: 1^2 + 2^2 + … + k^2

Написать функцию mylen которая считает длину списка/строки/tuple, без использования len.

Написать функцию mymin, для списков, без использования min/max.

Написать функцию add(nums1, nums2) которая возвращает сумму списков.

Input: [1, 5, 7], [10, 20, 50]
Output: [15, 25, 57]

Given k, create a list of form: [k, k-1, …, 3, 2, 1, 0, 1, 2, 3, … k-1, k]

Given nums, a list of numbers, and a number x, return True if nums contains x, otherwise False. Do not use methods of list or operator in.
'''

'''
Посчитать факториал k.
'''


def factorial(k):
    if k <= 0:
        return 1
    return k * factorial(k - 1)


print(factorial(5))

'''
Посчитать сумму: 1^2 + 2^2 + … + k^2
'''


def sum_alculation(k):
    if k <= 0:
        return 0
    return k ** 2 + sum_alculation(k - 1)


print(sum_alculation(5))

'''
Написать функцию mylen которая считает длину списка/строки/tuple, без использования len.
'''


def mylen(nums):
    if not nums:
        return 0
    return mylen(nums[1:]) + 1


print(mylen([1, 4, 6, 7, 5, 9]))

'''
Написать функцию mymin, для списков, без использования min/max.
'''


def mymin(nums: list) -> int:
    if len(nums) == 1:
        return nums[0]
    calc = mymin(nums[1:])
    return nums[0] if nums[0] < calc else calc


print(mymin([1, 3, 5]))

'''
Написать функцию add(nums1, nums2) которая возвращает сумму списков.
Input: [1, 5, 7], [10, 20, 50]
Output: [11, 25, 57]
'''


def myadd(nums1, nums2) -> list:
    if not (nums1 or nums2):
        return []
    if not nums1:
        return nums2
    if not nums2:
        return nums1

    return [nums1[0] + nums2[0]] + myadd(nums1[1:], nums2[1:])


print(myadd([1, 5, 7], [10, 20, 50, 7]))

'''
Given k, create a list of form: [k, k-1, …, 3, 2, 1, 0, 1, 2, 3, … k-1, k]
'''


def form(k) -> list:
    if k <= 0:
        return [0]
    return [k] + form(k - 1) + [k]


print(form(5))

'''
Given nums, a list of numbers, and a number x, return True if nums contains x, 
otherwise False. Do not use methods of list or operator in.
'''


def inside(nums, x) -> bool:
    if not nums:
        return False
    if nums[0] == x:
        return True
    if inside(nums[1:], x):
        return True
    else:
        False


print(inside([1, 6, 7, 8], 6))


def inside1(nums, x) -> bool:
    if not nums:
        return False
    return nums[0] == x or inside1(nums[1:], x)


print(inside1([1, 6, 7, 8], 6))

'''
Given a list, each its element either a number or a list of the same type. 
Compute sum of all the numbers in the list and it’s components.
'''


def sum_all(nums) -> int:
    if not nums:
        return 0
    if type(nums[0]) == int:
        return nums[0] + sum_all(nums[1:])
    return sum_all(nums[0]) + sum_all(nums[1:])


print(sum_all([[4], 6, 7]))

'''
Write a function flatten that given a list of numbers and nested 
list returns non-nested (flatten) list of all numbers.

Input: [[1, 2, 3], 10, 20, [100, [1000, 2000], 200], 30, 40]
Output: [1, 2, 3, 10, 20, 100, 1000, 2000, 200, 30, 40]

'''


def flatten(nums):
    if not nums:
        return []
    if isinstance(nums[0], list):
        return flatten(nums[0]) + flatten(nums[1:])
    return nums[:1] + flatten(nums[1:])


def flatten1(nums):
    res = []
    for num in nums:
        if isinstance(num, Iterable):
            res.extend(flatten1(num))
        else:
            res.append(num)
    return res


print("flatten1")

print(flatten1([range(10), {10, (100, 200)}]))
print(flatten1([[1, 2, 3], {10: 20, 5: 7, 40: 100}, [100, {1000, 2000}, 200], 30, 40]))


def sum_all(nums) -> int:
    if not nums:
        return 0
    if type(nums[0]) == int:
        return nums[0] + sum_all(nums[1:])
    return sum_all(nums[0]) + sum_all(nums[1:])


print(sum_all([[4], 6, 7]))
print(flatten1([1, 2, 3, 10, 20, [100, [1000, 2000], 200], 30, 40]))

'''
Write a function flatten that given a list of numbers and nested
list returns a sum of non-nested (flatten) list of all numbers.

Input: [[1, 2, 3], 10, 20, [100, [1000, 2000], 200], 30, 40]
Output: [1, 2, 3, 10, 20, 100, 1000, 2000, 200, 30, 40]
'''


def sum_flatten(nums: list) -> int:
    total = 0
    for num in nums:
        if isinstance(num, (list, tuple, set)):
            total += sum_flatten(num)
        else:
            total += num
    return total


print(sum_flatten([[1, 2, 3], 10, 20, [100, [1000, 2000], 200], 30, 40]))


def sum_flatten1(nums: Iterable) -> int:
    res = []
    for num in nums:
        if isinstance(num, Iterable):
            res.append(sum_flatten1(num))
        else:
            res.append(num)
    return sum(res)


print("sum")
print(sum_flatten1([range(10), {10, (100, 200)}]))
print(sum_flatten1([[1, 2, 3], 10, 20, [100, [1000, 2000], 200], 30, 40]))


def sum_flatten2(nums: list) -> int:
    '''
    res = []
    for num in nums:
        if isinstance(num, list):
            x = sum_flatten2(num)
        else:
            x = num
    res.append(x)
    res.append(sum_flatten2(num) if isinstance(num, list) else num)
    '''
    return sum(sum_flatten2(num) if isinstance(num, list) else num for num in nums)


print()
print(sum_flatten2([[1, 2, 3], 10, 20, [100, [1000, 2000], 200], 30, 40]))


def sum_of_nested(nums):
    return sum(sum_of_nested(num) if isinstance(num, Iterable) else num for num in nums)


print(sum_of_nested([[1, 2, 3], 10, 20, [100, (1000, 2000), 200], 30, 40]))
print(sum_of_nested([range(10), {10, (100, 200)}]))


def flatten0(nums):
    res = []
    for num in nums:
        try:
            res.extend(flatten0(num))
        except TypeError:
            res.append(num)
    return res


print(flatten0([[1, 2, 3], 10, 20, [100, (1000, 2000), 200], 30, 40]))
print(flatten0([range(10), {10, (100, 200)}]))
