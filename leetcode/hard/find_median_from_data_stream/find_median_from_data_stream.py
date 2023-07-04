import heapq


class MedianFinder1:
    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        if len(self.nums) % 2 == 1:
            # [10, 20, 30, 40, 50] = 5/2=2.5
            return self.nums[len(self.nums) // 2]
        else:
            # [10, 20, 30, 40] = 25
            return (self.nums[len(self.nums) // 2] + self.nums[len(self.nums) // 2 - 1]) / 2

    def __repr__(self) -> str:
        return f'{type(self).__qualname__}({self.nums})'


class MedianFinder2:
    def __init__(self):
        self.small = []  # Max Heap (-)
        self.large = []  # Min Heap
        '''
        max(self.small) <= min(self.large) 
        abs(len(self.small) - len(self.large)) <= 1       
        '''

    def addNum(self, num: int) -> None:
        heapq.heappush(self.large, num)
        if self.small and -self.small[0] > self.large[0]:
            heapq.heappush(self.small, -heapq.heappop(self.large))
        if abs(len(self.small) - len(self.large)) > 1:
            if len(self.small) < len(self.large):
                heapq.heappush(self.small, -heapq.heappop(self.large))
            else:
                heapq.heappush(self.large, -heapq.heappop(self.small))

    def findMedian(self) -> float:
        if len(self.large) > len(self.small):
            return self.large[0]
        elif len(self.large) < len(self.small):
            return -self.small[0]
        else:
            return (self.large[0] - self.small[0]) / 2

    def __repr__(self) -> str:
        return f'{type(self).__qualname__}({self.small}, {self.large})'


def test():
    for MedianFinder in MedianFinder1, MedianFinder2:
        median_finder = MedianFinder()
        print(median_finder)
        median_finder.addNum(1)  # arr = [1]
        median_finder.addNum(2)  # arr = [1, 2]
        print(median_finder)
        m = median_finder.findMedian()  # return 1.5(i.e., (1 + 2) / 2)
        assert m == 1.5
        median_finder.addNum(3)  # arr[1, 2, 3]
        m = median_finder.findMedian()  # return 2.0
        assert m == 2.0
        print(median_finder)


test()
