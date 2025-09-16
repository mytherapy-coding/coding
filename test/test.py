def len_str(s: str) -> int:
    print(s)
    if not s:
        return 0

    return len_str(s[1:]) + 1


print(len_str("hello"))


def find_elem(x, elems) -> bool:
    if not elems:
        return False
    return x == elems[0] or find_elem(x, elems[1:])


###


print(find_elem(15, [4, 6, 7, 5]))


def sum_calc(nums: list[int]) -> int:
    if not nums:
        return 0
    return sum_calc(nums[1:]) + nums[0]


print(sum_calc([1, 2, 3, 4]))


# quick sort
def sorting(values):
    if not values:
        return []
    p = values[0]
    less = [value for value in values if value < p]
    greater = [value for value in values if value > p]
    equal = [value for value in values if value == p]
    return sorting(less) + equal + sorting(greater)


"""
K(n) - number of recursion calls
n = len(values)
len(less) == len(right) == n/2
K(n) = 2 + 2K(n/2) = 
= 2 + 2(2 + 2K(n/2/2))=
= 2 + 4 + 4K(n/4)=
= 2+ 4+ 8 + 8K(n/8)=
let n = 2^p
= 2 + 4 + 8 + 16 + ... 2^i + 2^i*K(n/2^i)
assume i = p
= 2 + 4 + 8 + 16 + ... 2^p + 2^p*K(2^p/2^p)=
= 2 + 4 + 8 + 16 + ... 2^p + 2^p*K(1)=
= 2 + 4 + 8 + 16 + ... 2^p + 2^p*1=
= 2^p + 2^p + 2^p - 2 =
= 3* 2^p -2 = 3n -2 
s = 2 + 2 + 4 + 8 + 16 + ...+ 2^p = 2^p + 2^p


"""

"""
T(n)
time complexity of sorting(values)
where n = len(values)
we assume that len(less) == len(greater) ==n/2
T(n) = C*n + 2*T(n/2) 
= C*n + 2*(C*(n/2) + 2*T((n/2)/2))
= C*n + C*n + 4*T(n/4)
= C*n + C*n + 4*(C*n/4 + 2*T(n/4/2))=
= C*n + C*n + 4*C*n/4 + 8*T(n/8)=
= C*n + C*n + C*n + 8*T(n/8) = 
= ....=
= C*n * log n 
= 


 
"""


print(sorting([7, 9, 8, 0, 10, 3, 2]))

print("________________")


def merge_sort(values):
    if not values:
        return []
    if len(values) == 1:
        return [values[0]]
    left = values[: len(values) // 2]
    right = values[len(values) // 2 :]
    left = merge_sort(left)
    right = merge_sort(right)

    def merge(left: list[int], right: list[int]) -> list[int]:
        if not left or not right:
            return left + right
        if left[0] <= right[0]:
            return [left[0]] + merge(left[1:], right)
        return [right[0]] + merge(left, right[1:])

    return merge(left, right)


print(merge_sort([7, 9, 8, 0, 10, 3, 2]))


def factorial(n: int) -> int:
    # 1*2*3...
    if n == 0:
        return 1
    return factorial(n - 1) * n


print(factorial(5))


def log(n: int) -> int:
    # 2^k = n
    # 2^(k-1) = n /2
    if n == 1:
        return 0
    return log(n // 2) + 1


print(log(1024))


def reverse(s: str) -> str:
    if not s:
        return ""
    return s[-1] + reverse(s[:-1])


print(reverse("hello"))

count = 0


def merge(left: list[int], right: list[int]) -> list[int]:
    if not left or not right:
        return left + right
    if left[0] <= right[0]:
        return [left[0]] + merge(left[1:], right)
    return [right[0]] + merge(left, right[1:])


def merge1(left: list[int], right: list[int]) -> list[int]:
    def merge(i, j):
        # merge left[i:] right[j:]
        if i == len(left) or j == len(right):
            return left[i:] + right[j:]
        if left[i] <= right[j]:
            return [left[i]] + merge(i + 1, j)
        return [right[j]] + merge(i, j + 1)

    return merge(0, 0)


def merge2(left: list[int], right: list[int]) -> list[int]:
    merged = []

    def merge(i, j):
        if i == len(left) or j == len(right):
            merged.extend(left[i:])
            merged.extend(right[j:])
            return
        if left[i] <= right[j]:
            merged.append(left[i])
            merge(i + 1, j)
            return
        merged.append(right[j])
        merge(i, j + 1)

    merge(0, 0)
    return merged


def merge3(left: list[int], right: list[int]) -> list[int]:
    i = 0
    j = 0
    merged = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged


print()
print(merge([1, 3, 6, 8, 9, 11, 13, 16, 18, 79], [2, 4, 5, 7, 9, 13, 17, 23, 45, 78]))
print(merge1([1, 3, 6, 8, 9, 11, 13, 16, 18, 79], [2, 4, 5, 7, 9, 13, 17, 23, 45, 78]))
print(merge2([1, 3, 6, 8, 9, 11, 13, 16, 18, 79], [2, 4, 5, 7, 9, 13, 17, 23, 45, 78]))
print(merge3([1, 3, 6, 8, 9, 11, 13, 16, 18, 79], [2, 4, 5, 7, 9, 13, 17, 23, 45, 78]))


def find_min(nums):
    if len(nums) == 1:
        return nums[0]
    min_tail = find_min(nums[1:])
    return min_tail if min_tail <= nums[0] else nums[0]


def find_min1(nums):
    def find_min(i):
        # find minimum among nums[i:]
        if len(nums) - i == 1:
            return nums[-1]
        min_tail = find_min(i + 1)
        return min_tail if min_tail <= nums[i] else nums[i]

    return find_min(0)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(a[:-1])
print(a[1:])


"""
Написать функцию dupeach(values), которая создает список 2x размера, где каждый элемент из values дублирован.
Написать merge_ordered(values1, values2), которая берет два отсортированных списка и создает новый отсортированный 
список из элементов, каждый из которых находится в обоих списках values1 и values2.

"""
