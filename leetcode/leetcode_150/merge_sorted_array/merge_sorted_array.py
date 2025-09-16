def merge(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    if n == 0:
        return
    if m == 0:
        # for i in range(n):
        # nums1[i] = nums2[i]
        nums1[:n] = nums2[:n]
        return
    if nums1[m - 1] < nums2[n - 1]:
        nums1[m + n - 1] = nums2[n - 1]
        merge(nums1, m, nums2, n - 1)
    else:
        nums1[m + n - 1] = nums1[m - 1]
        merge(nums1, m - 1, nums2, n)


def merge2(nums1: list[int], m: int, nums2: list[int], n: int) -> None:
    i = m - 1
    j = n - 1
    k = m + n - 1
    while i >= 0 and j >= 0:
        if nums1[i] < nums2[j]:
            nums1[k] = nums2[j]
            j -= 1
        else:
            nums1[k] = nums1[i]
            i -= 1
        k -= 1
    if j >= 0:
        nums1[: j + 1] = nums2[: j + 1]


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
merge2(nums1, m, nums2, n)
print(nums1)
