def rotate(nums: list[int], k: int) -> None:
    for _ in range(k):
        tem = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = tem
    print(nums)

print(rotate([10, 20, 30, 40, 50], 3))


def rotate1(nums: list[int], k: int) -> None:
        k = k % len(nums)
        k = len(nums) - k 
        res = nums[k:] + nums[:k]
        for i in range(len(res)):
            nums[i] = res[i]

print(rotate1([10, 20, 30, 40, 50], 3))


def rotate2(nums: list[int], k: int) -> None:
    def reverse(beg: int, end: int, times: int = len(nums)) -> None:
        while times > 0 and beg < end:
            nums[beg], nums[end] = nums[end], nums[beg]
            beg += 1
            end -= 1
            times -= 1
        # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        #  [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    k %= len(nums)
    reverse(0, len(nums)-1, k)
    reverse(0, k-1)
    reverse(k, len(nums)-k-1)
    reverse(k, len(nums)-1)

print(rotate2([10, 20, 30, 40, 50], 3))