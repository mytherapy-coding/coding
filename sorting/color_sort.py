def two_color_sort(arr: list[int]):
    i = 0
    n = len(arr)
    j = n - 1
    while i < j:
        if arr[i] == 1 and arr[j] == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        if arr[i] == 0 and arr[j] == 0:
            i += 1
        if arr[i] == 1 and arr[j] == 1:
            j -= 1
        if arr[i] == 0 and arr[j] == 1:
            i += 1
            j -= 1


# Example usage
arr = [0, 1, 1, 1, 1, 1, 0, 0]
two_color_sort(arr)
print(arr)


def dutch_national_flag_sort(arr):
    low = 0  # next position for 0
    mid = 0  # current element
    high = len(arr) - 1  # next position for 2

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:  # arr[mid] == 2
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


# Example usage
arr = [0, 2, 1, 2, 0, 1, 0]
sorted_arr = dutch_national_flag_sort(arr)
print(sorted_arr)


def partition(nums: list[int], beg: int, end: int, pivot_ind: int) -> int:
    nums[end], nums[pivot_ind] = nums[pivot_ind], nums[end]
    pivot = nums[end]
    i = beg - 1
    for j in range(beg, end):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1], nums[end] = nums[end], nums[i + 1]
    return i + 1


def sort_012(arr: list[int]):
    def find(values):
        for i, x in enumerate(arr):
            if x in values:
                return i
        return None

    ind = find([0, 1])
    if ind is None:
        return

    pivot = arr[ind]
    ind = partition(arr, 0, len(arr) - 1, ind)
    if pivot == 0:
        ind1 = find([1])
        if ind1 is not None:
            partition(arr, ind + 1, len(arr) - 1, ind1)
    elif pivot == 1:
        ind0 = find([0])
        if ind0 is not None:
            partition(arr, 0, ind - 1, ind0)


arr = [1, 0, 2, 2, 1, 0, 1]
print("-------------")
sort_012(arr)
print(arr)


def two_color_sort(arr: list[int], beg: int, end: int, key):

    i = beg
    j = end
    while i < j:
        x = key(arr[i])
        y = key(arr[j])
        if x == 1 and y == 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        if x == 0 and y == 0:
            i += 1
        if x == 1 and y == 1:
            j -= 1
        if x == 0 and y == 1:
            i += 1
            j -= 1


def three_color_sort(arr: list[int]):

    two_color_sort(arr, 0, len(arr) - 1, key=lambda value: 1 if value > 0 else 0)

    two_color_sort(arr, 0, len(arr) - 1, key=lambda value: 1 if value > 1 else 0)


arr = [1, 0, 2, 2, 1, 0, 1]
print("++++++++")
three_color_sort(arr)
print(arr)
