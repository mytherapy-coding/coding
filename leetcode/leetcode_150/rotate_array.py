def rotate(nums: list[int], k: int) -> None:
    for _ in range(k):
        tem = nums[-1]
        for i in range(len(nums)-1, 0, -1):
            nums[i] = nums[i-1]
        nums[0] = tem
    print(nums)

print(rotate([10, 20, 30, 40, 50], 3))