import heapq
import collections


class SmallestInfiniteSet0:
    def __init__(self):
        self.nums = list(range(1, 1001))

    def popSmallest(self) -> int:
        smallest = min(self.nums)
        self.nums.remove(smallest)
        return smallest

    def addBack(self, num: int) -> None:
        if num not in self.nums:
            self.nums.append(num)


class SmallestInfiniteSet1:
    def __init__(self):
        self.nums = list(range(1, 1001))

    def popSmallest(self) -> int:
        return heapq.heappop(self.nums)  # O(log n)

    def addBack(self, num: int) -> None:  # O(n)
        if num not in self.nums:  # O(n)
            heapq.heappush(self.nums, num)  # O(log n)


class SmallestInfiniteSet2:
    def __init__(self):
        self.nums = list(range(1, 1001))
        self.unique = set(self.nums)
        # assert collections.Counter(self.nums) == collections.Counter(self.unique)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.nums)  # O(log n)
        self.unique.remove(smallest)  # O(1)
        # assert collections.Counter(self.nums) == collections.Counter(self.unique)
        return smallest

    def addBack(self, num: int) -> None:  # O(log n)
        if num not in self.unique:  # O(1)
            heapq.heappush(self.nums, num)  # O(log n)
            self.unique.add(num)  # O(1)
        # assert collections.Counter(self.nums) == collections.Counter(self.unique)


class SmallestInfiniteSet3:
    def __init__(self):
        self.nums = list(range(1, 11))
        self.unique = {k: 1 for k in self.nums}
        # assert collections.Counter(self.nums) == collections.Counter(self.unique)

    def popSmallest(self) -> int:
        smallest = heapq.heappop(self.nums)  # O(log n)
        del self.unique[smallest]  # O(1)
        # assert collections.Counter(self.nums) == collections.Counter(self.unique)
        return smallest

    def addBack(self, num: int) -> None:  # O(log n)
        if num not in self.unique:  # O(1)
            heapq.heappush(self.nums, num)  # O(log n)
            self.unique[num] = 1  # O(1)
        # assert collections.Counter(self.nums) == collections.Counter(self.unique)


class SmallestInfiniteSet4:
    def __init__(self):
        self.smallest = 0
        self.added_back = []

    def popSmallest(self) -> int:
        if self.added_back:
            smallest = min(self.added_back)  # O(n)
            self.added_back.remove(smallest)  # O(n)
            return smallest

        self.smallest += 1
        return self.smallest

    def addBack(self, num):
        if num <= self.smallest:
            if num not in self.added_back:  # O(n)
                self.added_back.append(num)  # O(1)


class SmallestInfiniteSet5:
    def __init__(self):
        self.smallest = 0
        self.added_back = []

    def popSmallest(self) -> int:
        if self.added_back:
            return heapq.heappop(self.added_back)  # O(log n)

        self.smallest += 1
        return self.smallest

    def addBack(self, num):
        if num <= self.smallest:
            if num not in self.added_back:  # O(n)
                heapq.heappush(self.added_back, num)  # O(log n)


class SmallestInfiniteSet6:
    def __init__(self):
        self.smallest = 0
        self.added_back = []
        self.unique = set()
        # assert collections.Counter(self.added_back) == collections.Counter(self.unique)
        # assert self.smallest >= max(self.added_back, default=0)

    def popSmallest(self) -> int:
        if self.added_back:
            self.unique.remove(self.added_back[0])
            smallest = heapq.heappop(self.added_back)  # O(log n)
            # assert collections.Counter(self.added_back) == collections.Counter(self.unique)
            # assert self.smallest >= max(self.added_back, default=0)
            return smallest
        self.smallest += 1
        # assert collections.Counter(self.added_back) == collections.Counter(self.unique)
        # assert self.smallest >= max(self.added_back, default=0)
        return self.smallest

    def addBack(self, num):  # O(log n)
        if num <= self.smallest:
            if num not in self.unique:  # O(1)
                heapq.heappush(self.added_back, num)  # O(log n)
                self.unique.add(num)  # O(1)
        # assert collections.Counter(self.added_back) == collections.Counter(self.unique), f'{self.added_back} {self.unique} {num=}'
        # assert self.smallest >= max(self.added_back, default=0)


def test():
    classes = [
        SmallestInfiniteSet0,
        SmallestInfiniteSet1,
        SmallestInfiniteSet2,
        SmallestInfiniteSet3,
        SmallestInfiniteSet4,
        SmallestInfiniteSet5,
        SmallestInfiniteSet6,
    ]
    for SmallestInfiniteSet in classes:
        smallestInfiniteSet = SmallestInfiniteSet()
        res = []
        smallestInfiniteSet.addBack(2)
        res.append(smallestInfiniteSet.popSmallest())
        res.append(smallestInfiniteSet.popSmallest())
        res.append(smallestInfiniteSet.popSmallest())
        smallestInfiniteSet.addBack(1)
        res.append(smallestInfiniteSet.popSmallest())
        res.append(smallestInfiniteSet.popSmallest())
        res.append(smallestInfiniteSet.popSmallest())
        print(res)
        assert res == [1, 2, 3, 1, 4, 5]


test()
