import heapq


def thirdMax0(nums: list[int]) -> int:
    unique = set(nums)
    res = []
    for _ in range(3):
        if not unique:
            return res[0]
        max_num = max(unique)
        unique.remove(max_num)
        res.append(max_num)
    return res[-1]


def thirdMax1(nums: list[int]) -> int:
    abc = sorted(set(nums))
    return abc[-3] if len(abc) >= 3 else abc[-1]


def thirdMax2(nums: list[int]) -> int:
    res = set()
    for num in nums:
        res.add(num)
        if len(res) > 3:
            res.remove(min(res))
    return max(res) if len(res) < 3 else min(res)


def thirdMax3(nums: list[int]) -> int:
    uniq = [-x for x in set(nums)]
    heapq.heapify(uniq)
    res = []
    for _ in range(min(len(uniq), 3)):
        res.append(-heapq.heappop(uniq))
    return max(res) if len(res) < 3 else min(res)


def test():
    for nums in [3, 2, 1], [1, 2], [2, 2, 3, 1], [1, 2, 2, 5, 3, 5]:
        for thirdmax in thirdMax0, thirdMax1, thirdMax2, thirdMax3:
            res = thirdmax(nums)
            print(f"nums: {nums}, thirdmax: {thirdmax.__name__}, result: {res}")


test()
