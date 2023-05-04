import itertools


def runningSum(nums: list[int]) -> list[int]:
    res = []
    for i in range(1, len(nums) + 1):
        res.append(sum(nums[:i]))
    return res


def runningSum2(nums: list[int]) -> list[int]:
    return [sum(nums[:i]) for i in range(1, len(nums) + 1)]


def runningSum3(nums: list[int]) -> list[int]:
    res = nums[:]
    for i in range(1, len(nums)):
        res[i] += res[i - 1]
    return res


def runningSum4(nums: list[int]) -> list[int]:
    res = [nums[0]]
    for i in range(1, len(nums)):
        res.append(res[i - 1] + nums[i])
    return res


def runningSum5(nums: list[int]) -> list[int]:
    return list(map(lambda i: sum(nums[:i]), range(1, len(nums) + 1)))


def runningSum6(nums: list[int]) -> list[int]:
    return list(itertools.accumulate(nums))


print(runningSum6([1, 2, 3, 4]))
