import itertools
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


def interlive0(values1: list, values2: list) -> list:
    if not values1 or not values2:
        return values1 + values2
    head = values1[0:1] + values2[0:1]
    tail = interlive0(values1[1:], values2[1:])
    print('govnoooo')
    print('tailllllll')
    print(values1, values2, head, tail)
    return head + tail


print(interlive0([30, 50, 70, 80], [4, 8]))


def interlive1(values1: list, values2: list) -> list:
    zipped = itertools.zip_longest(values1, values2)
    print('zippeddddd')
    # print(list(zipped))
    print(list(itertools.chain.from_iterable(zipped)))
    return [val for val in itertools.chain.from_iterable(zipped) if val is not None]


print('_________')
interlive1([30, 50, 70, 80], [4, 8])


def interlive2(values1: list, values2: list) -> list:
    if not values1 or not values2:
        return values1 + values2
    head = values1[0:1]
    tail = interlive2(values2, values1[1:])
    print(tail)
    return head + tail


print('??????')
print(interlive2([30, 50, 70, 80], [4, 8]))


def govno(n):
    for _ in range(n):
        print('#' * n)


govno(5)


def govno1(n, i=0):
    if i >= n:
        return
    print('#' * n)
    govno1(n, i + 1)


print('===========')
govno1(5)


def govno2(n):
    def f(i):
        if i >= n:
            return
        print('#' * n)
        f(i + 1)

    f(0)


print('===========')
govno2(3)

print('```````````````````')


def rombik(n):
    if n < 1:
        return
    print(n * '#')
    rombik(n - 1)


rombik(5)


def rombik(n):
    if n < 1:
        return

    print('#' * n)
    rombik(n - 1)
    print('#' * n)


rombik(5)


def rombik1():
    print('#')
    print('#')


def rombik2():
    print('##')
    rombik1()
    print('##')


def romnik(n):
    if n < 1:
        return
    print('#' * n)
    rombik(n - 1)
    print('#' * n)


print('!!!!!!!!!!!!!!!!!!')


def sum_even0(nums):
    if not nums:
        return 0
    res = 0
    if nums[0] % 2 == 0:
        res += nums[0]
    res += sum_even0(nums[1:])
    return res


print(sum_even0([20, 33, 50, 65, 70]))


def sum_even1(nums):
    if not nums:
        return 0
    res = 0
    if nums[0] % 2 == 0:
        res += nums[0]
    return res + sum_even1(nums[1:])


print(sum_even1([20, 33, 50, 65, 70]))


def sum_even2(nums):
    if not nums:
        return 0
    head = nums[0] * (nums[0] % 2 == 0)
    return head + sum_even2(nums[1:])


print(sum_even2([20, 33, 50, 65, 70]))


def sum_even3(nums):
    if not nums:
        return 0
    return nums[0] * (nums[0] % 2 == 0) + sum_even3(nums[1:])


print(sum_even3([20, 33, 50, 65, 70]))


def sum_even4(nums):
    return nums[0] * (nums[0] % 2 == 0) + sum_even4(nums[1:]) if nums else 0


print(sum_even3([20, 33, 50, 65, 70]))


def sum_even5(nums: list[int]) -> int:
    return sum(num for num in nums if num % 2 == 0)


print(sum_even5([20, 33, 50, 65, 70]))


def sum_even6(nums: list[int]) -> int:
    return sum(num * (num % 2 == 0) for num in nums)


print(sum_even6([20, 33, 50, 65, 70]))


def sum_odd(nums: list[int]) -> int:
    return sum(num * (num % 2) for num in nums)


print(sum_odd([20, 33, 50, 65, 70]))


def sum_even7(nums: list[int]) -> int:
    return sum(num * (num % 2) for num in nums)


print(sum_even7([20, 33, 50, 65, 70]))


def sum_even8(nums: list[int]) -> int:
    return sum(filter(lambda x: 1 - x % 2, nums))


print(sum_even8([20, 33, 50, 65, 70]))


def sum_even9(nums: list[int]) -> int:
    return sum(filter(lambda x: 1 - x & 1, nums))


print(sum_even9([20, 33, 50, 65, 70]))


def sum_even10(nums: list[int]) -> int:
    return sum(filter(lambda x: (x & 1) ^ 1, nums))


print(sum_even10([20, 33, 50, 65, 70]))

a = 14
b = 4

# 1110
# 100
# 0100
print(a and b)
print(b & a)

'''
decimal vs binary
0 -> 0
1 -> 1
2 -> 10
3 -> 11
4 -> 100
5 -> 101
6 -> 110
7 -> 111
8 -> 1000
9 -> 1001
10 -> 1010
11 -> 1011
12 -> 1100
13 -> 1101
14 -> 1110
15 -> 1111
16 -> 10000
'''


# sum_even10(nums: int) computes even numbers from nums
def sum_even10(nums: int):
    def f(beg: int) -> int:
        # f(beg) computes the sum of all even nums from nums[beg:]
        # f(0) computes the sum of all even nums from nums
        if beg >= len(nums):
            return 0
        head = nums[beg] if nums[beg] % 2 == 0 else 0
        return head + f(beg + 1)

    return f(0)


print(sum_even10([20, 33, 50, 65, 70]))

print('************************')


def even_numbers(nums: list[int]) -> list[int]:
    even_numbers = []
    for num in nums:
        if num % 2 == 0:
            even_numbers.append(num)
    return even_numbers


print(even_numbers([20, 33, 50, 65, 70]))


def even_numbers1(nums: list[int]) -> list[int]:
    return [num for num in nums if num % 2 == 0]


print(even_numbers1([20, 33, 50, 65, 70]))


def even_numbers2(nums: list[int]) -> list[int]:
    if not nums:
        return []
    even_numbers = []
    if nums[0] % 2 == 0:
        even_numbers.append(nums[0])
    even_numbers.extend(even_numbers2(nums[1:]))
    return even_numbers


print(even_numbers2([20, 33, 50, 65, 70]))


def even_numbers3(nums: list[int]) -> list[int]:
    if not nums:
        return []
    head = [nums[0]] if nums[0] % 2 == 0 else []
    return head + even_numbers3(nums[1:])


print(even_numbers3([20, 33, 50, 65, 70]))


def even_numbers4(nums: list[int]) -> list[int]:
    if not nums:
        return []
    head = [nums[0]] * (1 - nums[0] % 2)
    return head + even_numbers4(nums[1:])


print(even_numbers4([20, 33, 50, 65, 70]))


def even_numbers5(nums: list[int]) -> list[int]:
    return list(filter(lambda x: x % 2 == 0, nums))


print(even_numbers5([20, 33, 50, 65, 70]))


def even_numbers6(nums: list[int]) -> list[int]:  # time complexity 0(n^2)
    def f(n: int):
        '''
        [20, 33, 50, 65, 70] - nums
        [0,  1,  2,  3,  4] - indexes
        f(0) = []
        f(1) = [20]
        f(2) = [20]
        f(3) = [20, 50]
        f(4) = [20, 50]
        f(5) = [20, 50, 70]
        create an array with even numbers from nums[0:n]
        '''
        if n == 0:
            return []
        prefix_even = f(n - 1)
        tail = [nums[n - 1]] if nums[n - 1] % 2 == 0 else []
        return prefix_even + tail

    return f(len(nums))


print()
print(even_numbers6([20, 33, 50, 65, 70]))
'''
nums = [20, 33, 50, 65, 70]
print()
print(len(nums))
print(list(range(len(nums))))
print(list(range(5)))
print()
print(nums[:4])
print(list(range(4)))
print(range(4)) #- generator, same as [:4]

# [:4] - 4 elements
# index 4(fifth element in an array) -> 70
'''


def even_numbers7(nums: list[int]) -> list[int]:  # time complexity 0(n^2)
    def f(n: int):
        if n == 0:
            return []
        prefix_even = f(n - 1)
        tail = [nums[n - 1]] if nums[n - 1] % 2 == 0 else []
        res = prefix_even + tail
        return res

    return f(len(nums))


print(even_numbers7([10, 20]))
'''
len(nums) == 2


'''

def f(n):
    if n == 0:
        return
    print('----')
    print('*' * n, n)
    f(n - 1)
    print('#' * n, n)
f(5)

'''
s_len('') = 0
s_len(s) = s_len(s[1:]) + 1

'''
def s_len(s: str) -> int:
    if not s:
        return 0
    return s_len(s[1:]) + 1

print(len('govno'))

'''
SUM(a) = a0 + a1 + a1 + a2 + a3 + ... + a(n-2) + a(n-1) 
SUM(a[:n-1]) = a0 + a1 + a1 + a2 + a3 + ... +a(n-2) 
SUM([]) = 0
SUM(a) = SUM(a[:n-1]) + a(n-1) 

'''

def a_sum(a: list[int]) -> int:
    if not a:
        return 0
    return a_sum(a[:-1]) + a[-1]
'''

a_sum([10, 20, 30]) -> 60
  |
  if not [10, 20, 30] - False
  return a_sum([10, 20]) + 30 -> 30 + 30 = 60
    |
    if not [10, 20] - False
    return a_sum([10]) + 20 -> 10 + 20 = 30 
      |
      if not [10] - False
      return a_sum([]) + 10 -> 0 + 10 = 10 
        |
        if not [] - True
        return 0
          
  
  

'''




print(a_sum([2, 5, 7, 9]))

import calendar

print(calendar.isleap(2024))

'''
def isleap(year):
    """Return True for leap years, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

'''

'''
MIN(a) = min(a0, a1, a2, ... , a(n-2), a(n-1))
MIN(a[1:n]) = min(a1, a2, ... , a(n-2), a(n-1))
MIN(a) = a0 if len(a) = 1
MIN([x, y]) = x if x < y else y 
MIN(a) = MIN([a0, MIN(a[1:n])])

'''

def MIN(a: list[int]) -> int:
    if len(a) == 1:
        return a[0]
    if len(a) == 2:
        return a[0] if a[0] < a[1] else a[1]
    return MIN([a[0], MIN(a[1:])])


print(MIN([2, 6, 9, 54]))


'''
sum all positive numbers

SUM_POS(a)
'''

def sum_pos(a: list[int]) -> int:
    if not a:
        return 0
    if a[0] < 0:
        return sum_pos(a[1:])
    return sum_pos(a[1:]) + a[0]
'''
sum_pos([10, 20, -40, 30]) -> 60
  |
  if not a -> False
  if 10<0 -> False
  return sum_pos([20, -40, 30]) + 10 -> 50 + 10 = 60
    |
    if not a -> False
    if 20<0 -> False
    return sum_pos([-40, 30]) +20  -> 30 + 20 = 50
      |
      if not [-40, 30] ->  False
      if -40<0 -> True
      return sum_pos([30]) -> 30 
        | 
        if not [30] -> False
        if 30<0 -> False
        return sum_pos([]) + 30 -> 0 + 30 = 30 
          |
          if not[] -> True
          return 0        
        
        
'''




print(sum_pos([10, 20, -40, 30]))