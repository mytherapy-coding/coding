import heapq


class KthLargest0:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums, reverse=True)
        if len(self.nums) > self.k:
            del self.nums[self.k :]

    def add(self, val: int) -> int:
        self.nums.append(val)
        self.nums.sort(reverse=True)
        if len(self.nums) > self.k:
            self.nums.pop()
        return self.nums[-1]

    def __repr__(self):
        return f"{type(self).__qualname__}(k={self.k},nums={self.nums})"


class KthLargest1:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = nums[:]
        heapq.heapify(self.nums)
        for _ in range(len(self.nums) - k):
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        heapq.heappush(self.nums, val)
        if len(self.nums) > self.k:
            heapq.heappop(self.nums)
        return self.nums[0]

    def __repr__(self):
        return f"{type(self).__qualname__}(k={self.k},nums={self.nums})"


def test():
    for KthLargest in KthLargest0, KthLargest1:
        kth_largest = KthLargest(3, [4, 5, 8, 2])
        print(kth_largest.k, kth_largest.nums, kth_largest)
        res = []
        for value in 3, 5, 10, 9, 4:
            res.append(kth_largest.add(value))
        assert res == [4, 5, 5, 8, 8]
        print(res)


test()
