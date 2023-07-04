### Find Median from Data Stream

### Instructions
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.

For example, for arr = [2,3,4], the median is 3.
For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
Implement the MedianFinder class:

MedianFinder() initializes the MedianFinder object.
void addNum(int num) adds the integer num from the data stream to the data structure.
double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
### Example 1:

```
Input
["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
[[], [1], [2], [], [3], []]
Output
[null, null, null, 1.5, null, 2.0]

Explanation
MedianFinder medianFinder = new MedianFinder();
medianFinder.addNum(1);    // arr = [1]
medianFinder.addNum(2);    // arr = [1, 2]
medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
medianFinder.addNum(3);    // arr[1, 2, 3]
medianFinder.findMedian(); // return 2.0
```

### Constraints:
```
-105 <= num <= 105
There will be at least one element in the data structure before calling findMedian.
At most 5 * 104 calls will be made to addNum and findMedian.
```
### Solution
```py
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

```
* Time Complexity: O(n + k log n)
* Space Complexity: O(k) 

See other solutions in the Python file.


* [Source from Leedcode](https://leetcode.com/problems/find-median-from-data-stream/)





























